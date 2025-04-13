import requests

def enviar_telegram():
    token = "seu_token_do_bot"
    chat_id = "seu_chat_id"  # Você pode obter o seu chat_id a partir de conversas com o bot ou usando uma API
    mensagem = "Olá! Esta é uma mensagem enviada pelo meu script Python."

    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensagem}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Mensagem enviada com sucesso!")
        else:
            print("Falha ao enviar a mensagem:", response.status_code)
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")

# Chama a função para enviar a mensagem no Telegram
enviar_telegram()
