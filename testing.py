from pygame import mixer
import time, concurrent.futures, pyautogui, keyboard

def main(device):
    while True:
        while not keyboard.is_pressed("*"):
            time.sleep(0.1)

        print("Starting")
        mixer.init(devicename = device) # Initialize it with the correct device
        mixer.music.load("audio\gram.flac") # Load the mp3
        mixer.music.set_volume(0.06)
        mixer.music.play() # Play it

        pyautogui.keyDown('t')
        running = True
        while mixer.music.get_busy() and running:  # wait for music to finish playing
            time.sleep(0.1)
            if keyboard.is_pressed("-"):
                running = False
                print("Stopping")
                mixer.music.stop()
        pyautogui.keyUp('t')
        time.sleep(1)

if __name__ == "__main__":
    print("Started up...")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        devices = ["CABLE Input (VB-Audio Virtual Cable)", None]
        executor.map(main, devices)
        
