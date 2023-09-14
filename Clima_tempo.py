import subprocess
import sys

def instalar_pip():
    try:
        # Verifica se o pip já está instalado
        import pip
    except ImportError:
        # Baixa o script get-pip.py
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])
        print("pip foi instalado com sucesso!")

def instalar_requests():
    try:
        # Comando para instalar o pacote requests usando o pip
        comando = [sys.executable, "-m", "pip", "install", "requests"]

        # Executa o comando usando subprocess
        subprocess.check_call(comando)
        print("O pacote 'requests' foi instalado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao instalar 'requests': {e}")

# Instala o pip (caso não esteja instalado)
instalar_pip()

# Instala o pacote requests
instalar_requests()

import requests
from token_temp import api_key

# Obtenha o endereço IP do dispositivo
ip_info = requests.get("https://ipinfo.io")
data = ip_info.json()

# Extrai a latitude e a longitude do resultado
location = data.get("loc").split(",")
latitude = location[0]
longitude = location[1]

# Agora você pode usar latitude e longitude para consultar a API meteorológica
# Certifique-se de substituir 'SUA_CHAVE_DE_API' pela chave real da API meteorológica

weather_api_url = f'https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&apikey={api_key}'

# Realize uma solicitação HTTP para a API meteorológica
response = requests.get(weather_api_url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    weather_data = response.json()

    # Extraia o nome do local
    nome_local = weather_data.get("name")

    # Extraia os dados do primeiro intervalo de tempo (minutely[0])
    primeiro_intervalo = weather_data.get("timelines", {}).get("minutely", [])[0].get("values", {})

    if primeiro_intervalo:
        temperatura = primeiro_intervalo.get("temperature")
        umidade = primeiro_intervalo.get("humidity")
        velocidade_vento = primeiro_intervalo.get("windSpeed")

        # Exiba os dados do local e principais
        print(f"Local: {nome_local}")
        print("Dados Meteorológicos Principais:")
        print(f"Temperatura: {temperatura}°C")
        print(f"Umidade: {umidade}%")
        print(f"Velocidade do Vento: {velocidade_vento}")
    else:
        print("Dados do intervalo de tempo não encontrados")

else:
    print("Erro ao consultar a API meteorológica")