import csv
import subprocess
import time
from datetime import datetime

def coletar_ping():
    """Executa o ping e retorna tempo de resposta"""
    resultado = subprocess.run(["ping", "-n", "1", "www.google.com"], capture_output=True, text=True)
    linhas = resultado.stdout.split("\n")
    
    for linha in linhas:
        if "Tempo=" in linha:
            tempo = linha.split("Tempo=")[1].split("ms")[0].strip()
            return int(tempo)
    
    return None  # Retorna None se o ping falhar

def salvar_csv(nome_arquivo, timestamp, tempo):
    """Salva os dados no arquivo CSV"""
    with open(nome_arquivo, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, tempo])

# Loop infinito para rodar 24h por dia
data_atual = datetime.now().strftime("%Y-%m-%d")  # Define a data para nome do arquivo
nome_arquivo = f"ping_logs_{data_atual}.csv"  # Arquivo único por dia

# Criar CSV com cabeçalhos se ainda não existir
with open(nome_arquivo, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Latência (ms)"])

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tempo_ping = coletar_ping()

    if tempo_ping is not None:
        salvar_csv(nome_arquivo, timestamp, tempo_ping)
        print(f"[{timestamp}] Ping: {tempo_ping}ms - Salvo em {nome_arquivo}", flush=True)  # Exibir no terminal

    # Verifica se um novo dia começou e cria um novo arquivo CSV
    nova_data = datetime.now().strftime("%Y-%m-%d")
    if nova_data != data_atual:
        data_atual = nova_data
        nome_arquivo = f"ping_logs_{data_atual}.csv"

        # Criar novo CSV com cabeçalhos
        with open(nome_arquivo, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Latência (ms)"])

        print(f"\n🔄 Criando novo arquivo para o dia {data_atual}: {nome_arquivo}")

    time.sleep(1)  # Executa a cada 1 segundo
