from pytube import YouTube


def download_video_yt(url, path=''):
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(output_path=path)
        print("Descarga completa")
    except Exception as e:
        print("Error", e)


url_youtube = input("Dime la URL: ")  # Indicar la url del video
path = input("Indica la ruta: ")  # Indicar la ruta donde quieres descargar el video
download_video_yt(url_youtube, path)
