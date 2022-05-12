from time import sleep
import sounddevice as sd
from scipy.io.wavfile import write

while(1):
    fs = 44100  
    seconds = 5

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  
    write('output.wav', fs, myrecording)
    print("hihi")  
    sleep(60)
