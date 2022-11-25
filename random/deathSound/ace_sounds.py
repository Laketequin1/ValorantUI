import pyautogui, time
from pygame import mixer
import time, concurrent.futures, pyautogui, keyboard

def ace(device):
	print("Starting ace music")
	mixer.init(devicename = device) # Initialize it with the correct device
	mixer.music.load("audio\The Verkkars.mp3") # Load the mp3
	mixer.music.set_volume(1)
	mixer.music.play() # Play it

	pyautogui.keyDown('t')
	running = True
	while mixer.music.get_busy() and running:  # wait for music to finish playing
		time.sleep(0.1)
		if keyboard.is_pressed("*"):
			running = False
			print("Stopping ace music")
			mixer.music.stop()
	pyautogui.keyUp('t')

def outro(device):
	print("Starting ace music")
	mixer.init(devicename = device) # Initialize it with the correct device
	mixer.music.load("audio\Outro.mp3") # Load the mp3
	mixer.music.set_volume(0.5)
	mixer.music.play() # Play it

	pyautogui.keyDown('t')
	running = True
	while mixer.music.get_busy() and running:  # wait for music to finish playing
		time.sleep(0.1)
		if keyboard.is_pressed("*"):
			running = False
			print("Stopping ace music")
			mixer.music.stop()
	pyautogui.keyUp('t')

if __name__ == "__main__":
	print("Ace sounds")

	while True:
		image_list = list(pyautogui.locateAllOnScreen('ace.png', confidence=0.82))
		for image in image_list:
			if image.left > 907 and image.left < 905 or image.top > 179 and image.top < 177:
				continue
			print("Ace!")
			with concurrent.futures.ProcessPoolExecutor() as executor:
				devices = ["CABLE Input (VB-Audio Virtual Cable)", None]
				executor.map(ace, devices)
			break

		image_list = list(pyautogui.locateAllOnScreen('victory.png', confidence=0.82))
		for image in image_list:		
			if image.left > 598 and image.left < 595 or image.top > 483 and image.top < 475:
				continue
			print("End of game - Won!")
			with concurrent.futures.ProcessPoolExecutor() as executor:
				devices = ["CABLE Input (VB-Audio Virtual Cable)", None]
				executor.map(outro, devices)
			break
		
		image_list = list(pyautogui.locateAllOnScreen('defeat.png', confidence=0.82))
		for image in image_list:	
			if image.left > 635 and image.left < 630 or image.top > 483 and image.top < 475:
				continue
			print("End of game - Lost!")
			with concurrent.futures.ProcessPoolExecutor() as executor:
				devices = ["CABLE Input (VB-Audio Virtual Cable)", None]
				executor.map(outro, devices)
			break
			
