import subprocess
import os
import sys

STREAM_KEY = os.getenv("YOUTUBE_KEY")
VIDEO_FILE = "lo-fi.mp4"

def start_stream():
    if not STREAM_KEY:
        print("❌ ERRO: YOUTUBE_KEY não configurada!")
        sys.exit(1)
    
    if not os.path.exists(VIDEO_FILE):
        print(f"❌ ERRO: {VIDEO_FILE} não encontrado!")
        sys.exit(1)
    
    print("🎬 Iniciando transmissão...")
    
    # Comando SIMPLES - apenas vídeo
    cmd = [
        "ffmpeg",
        "-re",
        "-i", VIDEO_FILE,
        "-stream_loop", "-1",
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