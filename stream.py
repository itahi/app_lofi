import subprocess
import os
import time

# Configurações
STREAM_KEY = os.getenv("YOUTUBE_KEY")  # Vai no Railway
VIDEO_FILE = "lo-fi.mp4"  # Seu vídeo
IMAGE_FILE = "background.jpg"  # Ou use imagem estática

# Comando FFmpeg para live
def start_stream():
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
    subprocess.run(cmd)

if __name__ == "__main__":
    start_stream()