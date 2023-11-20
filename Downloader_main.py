import yt_dlp

# Download link
url = input("Digite o url:")


ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download concluído!")
