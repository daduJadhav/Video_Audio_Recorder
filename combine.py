import os
from moviepy.editor import *

class combine():
    def make(self,file_name):
        try:
            video = VideoFileClip('output.avi')
            audio = AudioFileClip('recording_1.wav')

            combineVideo = video.set_audio(audio)
            combineVideo.write_videofile(f"{file_name}.mp4")

            os.remove('output.avi')
            os.remove('recording_1.wav')
            print("Done!")

        except Exception as e:
            print(e)