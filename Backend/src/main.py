from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
driver = webdriver.Chrome(options=options)

# Dados da viagem, aonde origem e destino deve ser no modelo cidade-uf e a viagem sendo dd-m-yyyy
origem = "fortaleza-ce"
destino = "quixada-ce"
dataViagem = "19-4-2025"

# URL da busca com os parametros acima
url = f"https://viajeguanabara.com.br/onibus/{origem}/{destino}?departureDate={dataViagem}&passengers=1:1"
driver.get(url)

try:
    # Espera até que o elemento com as passagens esteja presente
    passagem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//app-trip")
        )
    )

    if passagem.text.strip():
        print(f"✅ Passagem existente para o dia {dataViagem}\n{passagem.text}")
    else:
        print(f"❌ Nenhuma passagem encontrada para o dia {dataViagem}")

except Exception as e:
    print(f"⚠️ Erro ao carregar a página ou não existe passagem para o dia {dataViagem}:")

finally:
    driver.quit()