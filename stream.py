import subprocess
import os
import time
import sys

# Configurações do Railway
STREAM_KEY = os.getenv("YOUTUBE_KEY")
VIDEO_FILE = "lo-fi.mp4"
IMAGE_FILE = "lofo.png"

def start_stream():
    # Verifica se a chave foi configurada
    if not STREAM_KEY:
        print("❌ ERRO: YOUTUBE_KEY não configurada!")
        print("Configure no Railway: Service > Variables")
        sys.exit(1)
    
    # Verifica se os arquivos existem
    if not os.path.exists(VIDEO_FILE):
        print(f"❌ ERRO: Arquivo {VIDEO_FILE} não encontrado!")
        sys.exit(1)
    
    if not os.path.exists(IMAGE_FILE):
        print(f"❌ ERRO: Arquivo {IMAGE_FILE} não encontrado!")
        sys.exit(1)
    
    print("✅ Arquivos verificados com sucesso!")
    print(f"📹 Vídeo: {VIDEO_FILE}")
    print(f"🖼️  Imagem: {IMAGE_FILE}")
    print(f"🔑 Stream Key: {STREAM_KEY[:10]}...")
    print("🎬 Iniciando transmissão...")
    
    cmd = [
        "ffmpeg",
        "-re",  # Lê no tempo real
        "-i", VIDEO_FILE,
        "-stream_loop", "-1",  # Loop infinito
        "-i", IMAGE_FILE,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-b:v", "2500k",
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "flv",
        f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
    ]
    
    print("🚀 Comando FFmpeg iniciado...")
    subprocess.run(cmd)

if __name__ == "__main__":
    start_stream()