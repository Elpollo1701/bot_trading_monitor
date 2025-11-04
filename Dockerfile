FROM python:3.10

WORKDIR /app

COPY bot.py /app

# Instala dependencias
RUN pip install flask prometheus_client

# Comando por defecto
CMD ["python", "bot.py"]
