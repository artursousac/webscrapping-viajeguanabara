import requests
from bs4 import BeautifulSoup

# origem e destino deve ser no formato cidade-uf, tudo minúsculo.
origem = "fortaleza-ce"
destino = "quixada-ce"
# Data deve ser no formato dd-m-yyy
dataViagem = "18-4-2025"

# URL contendo os parametros necessários do viaje-guanabara e realizando a requisição http
url = f"https://viajeguanabara.com.br/onibus/{origem}/{destino}?departureDate={dataViagem}&passengers=1:1"
response = requests.get(url)

# Se a response houver sucesso, analisa o HTML com o BeatifulSoup e extrai os dados necessários.
if response.status_code == 200:
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    paragrafo = soup.find('p')
    print(paragrafo.text)

# Se não tiver sucesso, informa que houve erro.
else:
    print("Erro ao acessar a página:", response.status_code)
