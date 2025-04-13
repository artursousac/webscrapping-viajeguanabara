from viajeguanabara import procurar_passagem
from telegram import enviar_telegram
from datetime import datetime
import os

procurar_passagem("fortaleza-ce", "quixada-ce", "18-4-2025")
procurar_passagem("quixada-ce", "fortaleza-ce", "21-4-2025")

try:
    caminho_log = 'Log.txt'
    with open(caminho_log, 'a') as log:
        log.write(f'Nova execucao: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n')
except:
    print("Erro")
