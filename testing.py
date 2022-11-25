import time, concurrent.futures
from pygame import mixer

def main(device):
    print("Starting")
    mixer.init(devicename = device) # Initialize it with the correct device
    mixer.music.load("audio\The Verkkars.mp3") # Load the mp3
    mixer.music.set_volume(0.8)
    mixer.music.play() # Play it

    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        devices = ["CABLE Input (VB-Audio Virtual Cable)", None]
        executor.map(main, devices)
        
