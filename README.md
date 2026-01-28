# Automação de Ponto Tangerino (Sólides)
Script em Python para registrar o ponto de forma automática e configurável, utilizando diretamente a API do sistema Tangerino.


### Descrição
Este projeto automatiza o processo de registro de ponto (entrada, almoço, volta, saída) no sistema Tangerino/Sólides. Ao invés de simular a navegação em um browser (via Selenium), este script faz requisições diretas à API do sistema, tornando o processo mais rápido, leve e confiável.

Ele foi projetado para rodar continuamente em um computador ou servidor, executando os registros nos horários pré-definidos e respeitando dias não úteis como finais de semana, feriados e períodos de férias.


### Funcionalidades
- Registro Automático: Registra o ponto nos horários especificados.

- Baseado em API: Não abre navegador, consome menos recursos e é mais estável.

- Agenda Configurável: Os horários de registro podem ser facilmente alterados no arquivo de configuração.

- Gestão de Dias de Folga:

    - Ignora automaticamente finais de semana.

    - Permite cadastrar feriados nacionais, estaduais e municipais.

    - Permite configurar períodos de férias ou licenças.

- Logging de Atividades: Todas as ações (tentativas de registro, sucessos, falhas, dias ignorados) são salvas em um arquivo de log (log_ponto_api.txt) para fácil verificação.


### Pré-requisitos
- Python 3.7+


### Instalação
1. Clone ou baixe este repositório:
```bash
# Se você tem Git
git clone <URL_DO_SEU_REPOSITORIO>

# Ou simplesmente baixe os arquivos ZIP e extraia
```

2. Navegue até a pasta do projeto:
```bash
cd caminho/para/a/pasta
```

3. Instale as dependências necessárias:
```bash
pip install requests schedule
```


### Configuração
Toda a configuração do script é feita no arquivo ``config.py``. Abra-o em um editor de texto e preencha as informações conforme as instruções abaixo.

1. Credenciais da API
Estas são as informações necessárias para autenticar sua requisição.
```bash
CODIGO_EMPREGADOR = "SEU_CODIGO"
PIN = "SEU_PIN"
FUNCIONARIO_ID = "SEU_ID_DE_FUNCIONARIO"
AUTHORIZATION_TOKEN = "Basic SEU_TOKEN_BASE64"
```

#### Como obter esses valores?

1. Acesse a página de registro de ponto do Tangerino pelo Google Chrome.

2. Abra as Ferramentas de Desenvolvedor (clique com o botão direito na página > Inspecionar > aba "Network" ou "Rede").

3. Faça o registro do ponto normalmente.

4. Na aba "Network", procure por uma requisição chamada ``sincronizacaoPontos``.

5. Clique nela e olhe as sub-abas "Headers" e "Payload" para encontrar todos os valores necessários.

ATENÇÃO: O ``AUTHORIZATION_TOKEN`` pode ser um token de sessão que expira após algum tempo. Se o script começar a falhar com erros de "Não Autorizado" (401 ou 403), você precisará obter um novo token repetindo os passos acima.


2. Horários de Registro
Defina os horários em que o ponto deve ser batido, no formato "HH:MM".

```bash
HORARIOS = [
    "08:00",
    "12:00",
    "13:00",
    "18:00"
]
```


3. Configuração de Dias de Folga
Defina as regras para os dias em que o ponto não deve ser registrado.

- ``DIAS_DA_SEMANA_A_IGNORAR``: Liste os dias da semana a serem ignorados (0=Segunda, 6=Domingo). Por padrão, Sábado (5) e Domingo (6) são ignorados.

- ``FERIADOS``: Adicione datas de feriados no formato "AAAA-MM-DD".

- ``PERIODOS_DE_FOLGA``: Adicione períodos de férias ou folgas no formato ("AAAA-MM-DD", "AAAA-MM-DD") para data de início e fim.


### Como Executar
1. Com o arquivo config.py devidamente preenchido, abra um terminal na pasta do projeto.

2. Execute o script principal:

```bash
python automacao_ponto_api.py
```

3. O script será iniciado e ficará rodando em segundo plano. Ele mostrará no terminal os agendamentos configurados.

4. O terminal precisa permanecer aberto para que o agendador continue funcionando. Para uma solução permanente em um servidor, considere usar ferramentas como systemd (Linux) ou NSSM (Windows).


### Avisos Importantes
- Uso por sua conta e risco: Você é responsável por garantir que os pontos estão sendo registrados corretamente. Verifique os logs e o portal do Tangerino periodicamente.

- Políticas da Empresa: Verifique se o uso de automação para registro de ponto é permitido pelas políticas da sua empresa.

- Mudanças na API: Se a Sólides/Tangerino alterar sua API, este script pode parar de funcionar e precisará de manutenção.