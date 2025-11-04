from flask import Flask
from prometheus_client import start_http_server, Counter, Gauge
import random, time, threading

app = Flask(__name__)

# Métricas
trades_total = Counter('bot_trades_total', 'Número total de trades ejecutados')
balance_gauge = Gauge('bot_balance', 'Balance actual del bot')

@app.route('/')
def home():
    return "🚀 Bot de Trading corriendo y enviando métricas a Prometheus"

def generar_metricas():
    balance = 100
    while True:
        trades_total.inc()  # Simula un trade
        balance += random.uniform(-1, 1)  # Simula cambio de balance
        balance_gauge.set(balance)
        time.sleep(5)  # Cada 5 segundos

if __name__ == "__main__":
    # Inicia servidor de métricas Prometheus en el puerto 8000
    start_http_server(8000)
    hilo = threading.Thread(target=generar_metricas)
    hilo.start()
    # Inicia servidor Flask en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
