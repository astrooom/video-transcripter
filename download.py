import os
from pytube import YouTube

current_dir = os.getcwd()
youtube_dl_path = os.path.join(current_dir, "yt-download")
def download_youtube_video_audio(url, dl_path):
    yt = YouTube(url)
    print(f"Grabbing audio from youtube video {yt.title}")
    audio_stream = yt.streams.get_audio_only()
    dl_filename = audio_stream.default_filename
    audio_stream.download(dl_path)
    print(dl_filename)
    return os.path.join(dl_path, dl_filename)