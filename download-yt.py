import yt_dlp

def baixar_video(url):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"Download concluído: {info.get('title', 'Vídeo')}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    video_url = input("URL do vídeo: ")
    baixar_video(video_url)
