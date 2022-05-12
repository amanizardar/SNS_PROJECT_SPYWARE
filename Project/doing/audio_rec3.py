from time import sleep
import sounddevice as sd
from scipy.io.wavfile import write

while(1):
    fs = 44100  
    seconds = 3 

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  
    write('output.wav', fs, myrecording)
    print("hihi")  
    sleep(60)


# import sounddevice
# from scipy.io.wavfile import write
# fs= 44100
# second =  int(input("Enter time duration in seconds: "))
# print("Recording.....n")
# record_voice = sounddevice.rec( int ( second * fs ) , samplerate = fs , channels = 2 )
# sounddevice.wait()
# write("out.wav",fs,record_voice)
# print("Finished.....nPlease check your output file")


# import sounddevice as sd
# import numpy as np
# import scipy.io.wavfile as wav

# fs=44100
# duration = 5  # seconds
# myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
# print ("Recording Audio")
# sd.wait()
# print ("Audio recording complete , Play Audio")
# sd.play(myrecording, fs)
# sd.wait()
# print ("Play Audio Complete")



# import pyaudio
# import wave

# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("* recording")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("* done recording")

# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()





# import pyaudio
# import wave

# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100

# def record():

# 	p = pyaudio.PyAudio()

# 	stream = p.open(format=FORMAT,
# 					channels=CHANNELS,
# 					rate=RATE,
# 					input=True,
# 					frames_per_buffer=CHUNK)

# 	print("Start recording")

# 	frames = []

# 	try:
# 		while True:
# 			data = stream.read(CHUNK)
# 			frames.append(data)
# 	except KeyboardInterrupt:
# 		print("Done recording")
# 	except Exception as e:
# 		print(str(e))

# 	sample_width = p.get_sample_size(FORMAT)
	
# 	stream.stop_stream()
# 	stream.close()
# 	p.terminate()
	
# 	return sample_width, frames	

# def record_to_file(file_path):
# 	wf = wave.open(file_path, 'wb')
# 	wf.setnchannels(CHANNELS)
# 	sample_width, frames = record()
# 	wf.setsampwidth(sample_width)
# 	wf.setframerate(RATE)
# 	wf.writeframes(b''.join(frames))
# 	wf.close()

# if __name__ == '__main__':
# 	print('#' * 80)
# 	print("Please speak word(s) into the microphone")
# 	print('Press Ctrl+C to stop the recording')
	
# 	record_to_file('output.wav')
	
# 	print("Result written to output.wav")
# 	print('#' * 80)