import os
import sys
from pathlib import Path

from convert import convert_to_wav_ffmpeg
from download import download_youtube_video_audio
from speech_recognizer import get_large_audio_transcription

current_dir = os.getcwd()
youtube_dl_path = os.path.join(current_dir, "yt-download")

mode = sys.argv[1]

################
# Youtube Mode #
################
if mode == "youtube":
    yt_url = sys.argv[2]
    downloaded_audio_path = download_youtube_video_audio(
        yt_url, youtube_dl_path)
    audio_file = downloaded_audio_path

#############
# File Mode #
#############
elif mode == "file":
    file = sys.argv[2]
    audio_file = file

################
# Invalid Mode #
################
else:
    print("Please select a valid mode. Available modes are: youtube, file")

##############################
# Convert audio file to .wav #
##############################
print(f"Converting {audio_file} to .wav")
converted_file_path = convert_to_wav_ffmpeg(audio_file)

#############################################
# Transcode in segments and get full output #
#############################################
transcribed_text = (get_large_audio_transcription(converted_file_path))

################################
# Output transcription to file #
################################
if not os.path.isdir(os.path.join(current_dir, "transcriptions")):
    os.mkdir(os.path.join(current_dir, "transcriptions"))
transcribe_textfile = os.path.join(
    current_dir, "transcriptions", f"{Path(converted_file_path).stem}.txt")
with open(transcribe_textfile, 'wt') as out:
    out.write(transcribed_text)
