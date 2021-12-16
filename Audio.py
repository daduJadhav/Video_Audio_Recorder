import sounddevice as sd
import wavio as wv

class AudioRecorder():
    def __init__(self) -> None:

        self.frequency = 44100
        self.duration = 10

    def record(self):
        recording = sd.rec(int(self.duration * self.frequency),
        samplerate=self.frequency, channels = 2)

        sd.wait()

        wv.write("recording_1.wav",recording,self.frequency,sampwidth = 2)

        return True