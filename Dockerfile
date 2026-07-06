# Usa uma imagem base leve com Python
FROM python:3.11-slim

# Instala o FFmpeg (essencial!)
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Define o diretório de trabalho
WORKDIR /app

# Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia seu código
COPY . .

# Expõe a porta que o Railway vai usar
EXPOSE $PORT

# Comando para iniciar sua live
CMD ["python", "stream.py"]