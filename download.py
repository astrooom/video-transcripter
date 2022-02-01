import os
import yt_dlp

# DEPRECATED
# def download_youtube_video_audio(url, dl_path):
#     yt = YouTube(url)
#     print(f"Grabbing audio from youtube video {yt.title}")
#     audio_stream = yt.streams.get_audio_only()
#     dl_filename = audio_stream.default_filename
#     audio_stream.download(dl_path)
#     print(dl_filename)
#     return os.path.join(dl_path, dl_filename)

def download_youtube_video_audio(url, dl_path):
    options = {
        'format': 'bestaudio/best',  # choice of quality
        'extractaudio': True,        # only keep the audio
        'outtmpl': f'{dl_path}/' + '%(title)s.%(ext)s' # set download location
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        dl_filename = ydl.prepare_filename(info)
        ydl.download([url])

    return os.path.join(dl_path, dl_filename) 