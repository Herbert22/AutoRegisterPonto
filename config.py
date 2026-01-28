# -- INFORMAÇÕES DA API E CREDENCIAIS --
CODIGO_EMPREGADOR = "F22QC"
PIN = "4864"
FUNCIONARIO_ID = "3520536"
AUTHORIZATION_TOKEN = "Basic MzUyMDUzNjpQCMjRQw=="
URL_PONTO = "https://app.tangerino.com.br/Tangerino/pages/login/"

# -- HORÁRIOS PARA REGISTRO DE PONTO (formato 24h) --
HORARIOS = [
    "08:00",
    "12:00",
    "14:50",
    "18:00"
]
PAUSA_CAPTCHA_SEGUNDOS = 1

# --------------------------------------------------------------------
# -- CONFIGURAÇÃO DE DIAS A NÃO REGISTRAR O PONTO --
# --------------------------------------------------------------------

# 1. DIAS DA SEMANA: Liste os dias da semana a serem ignorados.
# Onde: 0=Segunda, 1=Terça, 2=Quarta, 3=Quinta, 4=Sexta, 5=Sábado, 6=Domingo
# Exemplo para ignorar Sábados e Domingos: [5, 6]
DIAS_DA_SEMANA_A_IGNORAR = [5, 6]

# 2. FERIADOS: Liste as datas específicas de feriados.
# Formato: "AAAA-MM-DD"
FERIADOS = [
    "2025-01-01",  # Confraternização Universal
    "2025-03-03",  # Carnaval
    "2025-03-04",  # Carnaval
    "2025-04-18",  # Paixão de Cristo
    "2025-04-21",  # Tiradentes
    "2025-05-01",  # Dia do Trabalho
    "2025-06-19",  # Corpus Christi
    "2025-07-02",  # Independência da Bahia
    "2025-09-07",  # Independência do Brasil
    "2025-10-12",  # Nossa Senhora Aparecida
    "2025-11-02",  # Finados
    "2025-11-15",  # Proclamação da República
    "2025-11-20",  # Dia da Consciência Negra (se for feriado na sua cidade/estado)
    "2025-12-08",  # Nossa Senhora da Conceição da Praia
    "2025-12-25",  # Natal
]

# 3. PERÍODOS DE FOLGA (FÉRIAS, LICENÇAS, ETC):
# Liste os períodos como uma data de início e uma data de fim.
# O script não registrará o ponto em nenhum dia dentro desses intervalos (incluindo as datas de início e fim).
# Formato: [("AAAA-MM-DD", "AAAA-MM-DD")]
PERIODOS_DE_FOLGA = [
    ("2025-07-15", "2025-07-30"),  # Exemplo de período de férias
    # ("2025-12-26", "2026-01-05"), # Exemplo de recesso de fim de ano
]

# --------------------------------------------------------------------
# -- CONFIGURAÇÃO DE RETENTATIVA AUTOMÁTICA --
# --------------------------------------------------------------------

# Número máximo de vezes que o script tentará registrar o ponto em caso de falha de rede.
# Se a primeira tentativa falhar, ele tentará mais (MAX_TENTATIVAS - 1) vezes.
# Colocar 1 desativa as retentativas.
MAX_TENTATIVAS = 3

# Intervalo em minutos que o script aguardará antes de tentar novamente.
INTERVALO_TENTATIVAS_MINUTOS = 5