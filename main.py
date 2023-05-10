import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound
import time

def recording_sound(seconds,file_name):
    fs = 48000  # Sample rate
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    print("Recording...")
    sd.wait()  # Wait until recording is finished
    write(file_name+'.wav', fs, myrecording)  # Save as WAV file
    print(f"The sound file named {file_name} is saving...")
    time.sleep(3)
    print(f"The sound file named {file_name} has been saved.")

def playing_sound(file_name):
    print(f"Playing {file_name}")
    playsound(file_name+'.wav')

while True:
    print("""
    Welcome to my MusicBox!
    Please select your progress
    1) Recording
    2) Playing
    3) Quit
    """)
    choice = input("Choice : ")
    if choice == "1":
        seconds = int(input("Duration of recording (sec): "))
        file_name = input("Enter file name : ")
        recording_sound(seconds,file_name)
    elif choice == "2":
        file_name = input("Enter file name : ")
        playing_sound(file_name)

    elif choice == "3":
        print("See You Soon...\nQuiting...")
        time.sleep(2)
        break
    else:
        print("Invalid Choice")






















