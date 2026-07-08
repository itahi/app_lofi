import subprocess
import os
import sys

STREAM_KEY = os.getenv("YOUTUBE_KEY")
VIDEO_FILE = "lo-fi.mp4"
IMAGE_FILE = "lofo.png"

def start_stream():
    if not STREAM_KEY:
        print("❌ ERRO: YOUTUBE_KEY não configurada!")
        sys.exit(1)
    
    if not os.path.exists(VIDEO_FILE):
        print(f"❌ ERRO: {VIDEO_FILE} não encontrado!")
        sys.exit(1)
    
    if not os.path.exists(IMAGE_FILE):
        print(f"❌ ERRO: {IMAGE_FILE} não encontrado!")
        sys.exit(1)
    
    print("✅ Arquivos verificados!")
    print(f"📹 Vídeo: {VIDEO_FILE} (em loop)")
    print(f"🖼️ Imagem: {IMAGE_FILE}")
    print("🎬 Iniciando transmissão...")
    
    # Comando com LOOP + OVERLAY
    cmd = [
        "ffmpeg",
        "-re",
        "-stream_loop", "-1",        # 🔁 LOOP INFINITO
        "-i", VIDEO_FILE,
        "-i", IMAGE_FILE,
        "-filter_complex",
        "[1:v]scale=200:200[img];[0:v][img]overlay=W-w-20:H-h-20",
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