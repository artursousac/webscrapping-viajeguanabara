import requests

def enviar_telegram(mensagem):
    token = "seu_token_do_bot"
    chat_id = "seu_chat_id"
    message = mensagem
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Mensagem enviada com sucesso!")
        else:
            print("Falha ao enviar a mensagem:", response.status_code)
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")
