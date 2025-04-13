from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telegram import enviar_telegram
from dotenv import load_dotenv
import os

load_dotenv()
token_telegram = os.getenv("TOKEN_TELEGRAM")
chat_id_telegram_1 = os.getenv("CHAT_ID_1")
chat_id_telegram_2 = os.getenv("CHAT_ID_2")

def procurar_passagem(origem, destino, dataViagem):
    options = Options()
    driver = webdriver.Chrome(options=options)

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
            enviar_telegram(f"✅ Passagem existente para o dia {dataViagem}\n{passagem.text}", token_telegram, chat_id_telegram_1, chat_id_telegram_2)
        else:
            print(f"❌ Nenhuma passagem encontrada para o dia {dataViagem}")

    except Exception as e:
        print(f"⚠️ Erro ao carregar a página ou não existe passagem para o dia {dataViagem}")

    finally:
        driver.quit()