import threading,time
from sounddevice import rec            # this is to join two function with each other parallely .
from Audio import AudioRecorder
from Video import Video
from combine import combine 

aud = AudioRecorder()
vid = Video()
combin = combine()

def Audio():
    aud.record()

def vodeoRec ():
    vid.record()
   

if __name__ == '__main__':

    t1 = threading.Thread(target=Audio)

    t2 = threading.Thread(target=vodeoRec)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    time.sleep(5)
    combin.make("Video")