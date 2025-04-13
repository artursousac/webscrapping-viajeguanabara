import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações do navegador
options = Options()
options.add_argument("--headless")  # Deixe comentado se quiser ver o navegador
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

# Acessa o site
url = "https://quotes.toscrape.com"
driver.get(url)

try:
    # Espera até que todas as tags de citação estejam visíveis
    time.sleep(2)

    # Procura por citações com a tag 'life'
    tags = driver.find_element(By.CLASS_NAME, "header")

    print(tags.text)

except Exception as e:
    print("⚠️ Erro ao carregar a página ou encontrar elementos:", e)

# Fecha o navegador
driver.quit()
