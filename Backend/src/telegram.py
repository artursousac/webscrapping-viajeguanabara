import requests

def enviar_telegram(mensagem, token, chat_id_1, chat_id_2):
    message = mensagem
    url_1 = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_1}&text={message}"
    url_2 = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_2}&text={message}"

    try:
        response_1 = requests.get(url_1)
        response_2 = requests.get(url_2)
        if response_1.status_code == 200 and response_2.status_code == 200:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Falha ao enviar a mensagem: {response_1, response_2}")
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")

def enviar_telegram_unico(mensagem, token, chat_id):
    message = mensagem
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Falha ao enviar a mensagem: {response}")
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")