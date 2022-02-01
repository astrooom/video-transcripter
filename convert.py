import os
import ffmpeg

# Convert input file (can be both a video and an audio file) to .wav
def convert_to_wav_ffmpeg(video_file, output_ext="wav"):
    convert_dir = os.path.dirname(video_file)
    filename, ext = os.path.splitext(video_file)
    input = ffmpeg.input(video_file)
    audio = input.audio
    stream = ffmpeg.output(audio, f"{filename}.{output_ext}", acodec="pcm_s16le")
    ffmpeg.run(stream, quiet=True)
    output_file = (os.path.join(convert_dir, f"{filename}.{output_ext}"))
    return output_file # Returns the path to use in the main script