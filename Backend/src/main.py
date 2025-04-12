import requests
from bs4 import BeautifulSoup

# origem e destino deve ser no formato cidade-uf, tudo minúsculo.
origem = "fortaleza-ce"
destino = "quixada-ce"
# Data deve ser no formato dd-m-yyy
dataViagem = "18-4-2025"

url = f"https://viajeguanabara.com.br/onibus/{origem}/{destino}?departureDate={dataViagem}&passengers=1:1"
response = requests.get(url)

# 2. Verificar se deu certo
if response.status_code == 200:
    html = response.text

    # 3. Analisar o HTML
    soup = BeautifulSoup(html, 'html.parser')

    # 4. Extrair os dados (exemplo: o primeiro parágrafo)
    paragrafo = soup.find('p')
    print(paragrafo.text)
else:
    print("Erro ao acessar a página:", response.status_code)
