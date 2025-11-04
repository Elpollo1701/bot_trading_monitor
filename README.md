# Bot Trading Monitor

Proyecto de ejemplo que integra un **bot de trading simulado** con **Prometheus** para métricas y **Grafana** para visualización y dashboards en tiempo real.  
Este proyecto utiliza **Docker** y **docker-compose** para levantar todos los servicios de manera fácil y reproducible.
---
## 🧩 Contenido del repositorio
- `bot.py` → Bot de trading simulado con métricas Prometheus y servidor web Flask.  
- `Dockerfile` → Imagen Docker del bot.  
- `docker-compose.yml` → Levanta bot, Prometheus y Grafana en contenedores.  
- `prometheus.yml` → Configuración de Prometheus para leer métricas del bot.  
- `.gitignore` → Archivos que no se suben al repositorio.  

---
## 🚀 Cómo levantar el proyecto
1. Clonar el repositorio:

```bash
git clone https://github.com/Elpollo1701/bot_trading_monitor.git
cd bot_trading_monitor

Levantar los contenedores con Docker Compose:
docker-compose up -d --build

Verificar que los contenedores estén corriendo:
docker ps

Acceder a los servicios
Bot Flask (simulación web): http://localhost:5000
Métricas Prometheus: http://localhost:8000/metrics
Prometheus: http://localhost:9090
Grafana: http://localhost:3000
Usuario: admin
Contraseña: admin

📊 Crear dashboards en Grafana
Abrir Grafana → Configuration → Data Sources → Add data source → Prometheus
URL: http://prometheus:9090
Guardar y probar conexión
Crear un nuevo dashboard:
Métrica ejemplo: bot_balance → línea de tiempo, Gauge o Stat
Métrica ejemplo: rate(bot_trades_total[1m]) → trades por minuto
Guardar dashboard y agregar paneles según tus métricas.

💡 Métricas disponibles
bot_trades_total → Número total de trades ejecutados
bot_balance → Balance actual del bot
rate(bot_trades_total[1m]) → Trades por minuto
avg_over_time(bot_balance[5m]) → Promedio del balance últimos 5 min

⚡ Buenas prácticas
Actualiza el .gitignore si agregas archivos temporales o credenciales.
Para cambios en el bot o métricas, haz commit y push a GitHub:
git add .
git commit -m "Descripción del cambio"
git push

📝 Notas
Este proyecto es educativo y de pruebas, pero sirve como base para monitorizar bots reales,
integrando métricas Prometheus y dashboards Grafana de manera profesional.
