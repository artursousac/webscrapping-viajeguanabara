from viajeguanabara import procurar_passagem
from datetime import datetime
import os

procurar_passagem("fortaleza-ce", "quixada-ce", "18-4-2025")
procurar_passagem("quixada-ce", "fortaleza-ce", "21-4-2025")

caminho_log = os.path.join(os.path.dirname(__file__), '..', 'dist', 'Log.txt')
with open(caminho_log, 'a') as log:
    log.write(f'Nova execução: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n')
