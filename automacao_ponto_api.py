import time
import schedule
import logging
from datetime import date, datetime

# Importações do Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Importa as configurações
from config import (
    URL_PONTO, CODIGO_EMPREGADOR, PIN, HORARIOS,
    DIAS_DA_SEMANA_A_IGNORAR, FERIADOS, PERIODOS_DE_FOLGA,
    MAX_TENTATIVAS, INTERVALO_TENTATIVAS_MINUTOS
)

# Configuração de logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("log_ponto_selenium.txt"),
                        logging.StreamHandler()
                    ])

def registrar_ponto_selenium():
    """
    Abre o navegador, preenche os dados e clica no botão 'Registrar',
    respeitando dias de folga e com lógica de retentativa.
    """
    
    # --- Verificação de dia útil (lógica que já tínhamos) ---
    hoje = date.today()
    hoje_str = hoje.strftime("%Y-%m-%d")
    if hoje.weekday() in DIAS_DA_SEMANA_A_IGNORAR or hoje_str in FERIADOS:
        logging.info(f"Hoje ({hoje_str}) é um dia configurado para não bater ponto. Nenhuma ação será tomada.")
        return
    for inicio_str, fim_str in PERIODOS_DE_FOLGA:
        if datetime.strptime(inicio_str, "%Y-%m-%d").date() <= hoje <= datetime.strptime(fim_str, "%Y-%m-%d").date():
            logging.info(f"Hoje ({hoje_str}) está dentro de um período de folga/férias. Nenhuma ação será tomada.")
            return
            
    logging.info("Hoje é um dia de trabalho. Iniciando o processo de registro de ponto via Selenium...")
    
    # --- Lógica de Retentativa ---
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        driver = None
        try:
            logging.info(f"Tentativa {tentativa} de {MAX_TENTATIVAS}...")
            
            service = Service(executable_path='./chromedriver')
            options = webdriver.ChromeOptions()
            # options.add_argument('--headless') # Descomente para rodar sem abrir a janela do navegador (pode não funcionar com CAPTCHA)
            driver = webdriver.Chrome(service=service, options=options)
            
            driver.get(URL_PONTO)
            wait = WebDriverWait(driver, 20)
            
            # Preenche os campos
            wait.until(EC.presence_of_element_located((By.ID, "codigoEmpregador"))).send_keys(CODIGO_EMPREGADOR)
            driver.find_element(By.ID, "codigoPin").send_keys(PIN)
            logging.info("Campos preenchidos.")
            time.sleep(1)
            
            # Clica no botão de registrar
            wait.until(EC.element_to_be_clickable((By.ID, "registraPonto"))).click()
            logging.info("Botão 'Registrar' clicado.")
            
            # IMPORTANTE: Espera por uma mensagem de sucesso
            # Você precisa descobrir o ID ou outra característica da mensagem de sucesso que aparece na tela.
            # Inspecione o elemento (botão direito > Inspecionar) e troque o 'id_da_mensagem_de_sucesso' abaixo.
            wait.until(EC.presence_of_element_located((By.ID, "id_da_mensagem_de_sucesso")))
            
            logging.info("Ponto registrado com SUCESSO!")
            break  # Sai do loop de tentativas se teve sucesso

        except (TimeoutException, NoSuchElementException) as e:
            logging.warning(f"Falha na tentativa {tentativa}: Não foi possível encontrar um elemento na página ou o tempo de espera esgotou. Erro: {e}")
            if tentativa == MAX_TENTATIVAS:
                logging.error("Todas as tentativas falharam. Desistindo deste registro.")
            else:
                logging.info(f"Aguardando {INTERVALO_TENTATIVAS_MINUTOS} minutos para a próxima tentativa...")
                time.sleep(INTERVALO_TENTATIVAS_MINUTOS * 60)
        except Exception as e:
            logging.error(f"Ocorreu um erro inesperado: {e}")
            break # Sai do loop em caso de erro desconhecido
        finally:
            if driver:
                driver.quit() # Garante que o navegador sempre será fechado

# O resto do arquivo permanece igual
def agendar_tarefas():
    schedule.clear()
    for horario in HORARIOS:
        schedule.every().day.at(horario).do(registrar_ponto_selenium)
        logging.info(f"Registro de ponto agendado para as {horario}.")

if __name__ == "__main__":
    agendar_tarefas()
    logging.info("Automação via Selenium iniciada. Aguardando horários agendados...")
    while True:
        schedule.run_pending()
        time.sleep(1)