import pyautogui, time
from pygame import mixer
import time, concurrent.futures, pyautogui, keyboard

def main(device):
	print("Starting music")
	mixer.init(devicename = device) # Initialize it with the correct device
	mixer.music.load("audio\The Verkkars.mp3") # Load the mp3
	mixer.music.set_volume(0.2)
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

if __name__ == "__main__":
	print("Ace sounds")

	while True:
		image_list = list(pyautogui.locateAllOnScreen('ace.png', confidence=0.82))
		for image in image_list:
			if image.left > 907 and image.left < 905:
				continue
			if image.top > 179 and image.top < 177:
				continue
			print("Ace!")
			with concurrent.futures.ProcessPoolExecutor() as executor:
				devices = ["CABLE Input (VB-Audio Virtual Cable)", None]
				executor.map(main, devices)
				time.sleep(30)
			break
		
