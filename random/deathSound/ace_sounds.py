import pyautogui, time, random, concurrent.futures, keyboard, pyscreeze
from pygame import mixer
from PIL import ImageGrab

IMAGES = {'images/ace.png':(904, 177, 111, 74), 'images/victory.png':(594, 471, 731, 132), 'images/defeat.png':(632, 475, 665, 127), 'images/spectate.png':(133, 850, 19, 26)}

def ace(device):
	mixer.init(devicename = device) # Initialize it with the correct device
	mixer.music.load("audio/The Verkkars.mp3") # Load the mp3
	mixer.music.set_volume(1.5)
	mixer.music.play() # Play it

	pyautogui.keyDown('t')
	running = True
	while mixer.music.get_busy() and running:  # wait for music to finish playing
		pyautogui.keyDown('t')
		time.sleep(0.1)
		if keyboard.is_pressed("*"):
			running = False
			print("Stopping ace music")
			mixer.music.stop()
	pyautogui.keyUp('t')

def outro(device):
	mixer.init(devicename = device) # Initialize it with the correct device
	mixer.music.load("audio/Outro.mp3") # Load the mp3
	mixer.music.set_volume(0.6)
	mixer.music.play() # Play it

	pyautogui.keyDown('t')
	running = True
	while mixer.music.get_busy() and running:  # wait for music to finish playing
		pyautogui.keyDown('t')
		time.sleep(0.1)
		if keyboard.is_pressed("*"):
			running = False
			print("Stopping ace music")
			mixer.music.stop()
	pyautogui.keyUp('t')

def kill(device):
	mixer.init(devicename = device) # Initialize it with the correct device
	mixer.music.load(f"audio/Enemy/enemy ({random.randint(1, 41)}).mp3") # Load the mp3
	mixer.music.set_volume(2.5)
	mixer.music.play() # Play it

	pyautogui.keyDown('t')
	running = True
	while mixer.music.get_busy() and running:  # wait for music to finish playing
		pyautogui.keyDown('t')
		time.sleep(0.1)
		if keyboard.is_pressed("*"):
			running = False
			print("Stopping ace music")
			mixer.music.stop()
	pyautogui.keyUp('t')

def get_images(image, box):		
	return pyautogui.locateOnScreen(image, confidence=0.8, region=box)

def get_kills(box):
	pic = ImageGrab.grab(bbox = box)

	for i in range(22):
		image = pyscreeze.locate(f'images/kills/kill{i}.png', pic, confidence=0.7)
		if image:
			return True

if __name__ == "__main__":
	print("Ace sounds")

	devices = ["CABLE Input (VB-Audio Virtual Cable)"]

	last_tick = {'kill': 0, 'ace': 0, 'end': 0}

	with concurrent.futures.ProcessPoolExecutor() as executor:
		while True:
			this_tick = {'kill': False, 'ace': False, 'end': False}
			located_images = {}
			
			with concurrent.futures.ThreadPoolExecutor(max_workers=round(len(IMAGES.keys())/2)) as executor_mini:
				for image, box in zip(IMAGES.keys(), IMAGES.values()):
					located_images[image] = executor_mini.submit(get_images, image, box)
				located_images["kill"] = executor_mini.submit(get_kills, (890, 790, 1010, 910))
			
			if located_images['kill'].result():
				spectating = False
				if located_images['images/spectate.png'].result():
					spectating = True
				if not spectating and not last_tick['kill']:
					print("Kill!")
					executor.map(kill, devices)
				this_tick['kill'] = True
			if not this_tick['kill']:
				if last_tick['kill'] > 0:
					last_tick['kill'] -= 1
			else:
				last_tick['kill'] = 2

			if located_images['images/ace.png'].result():
				if not last_tick['ace']:
					print("Ace!")
					executor.map(ace, devices)
				this_tick['ace'] = True
			if not this_tick['ace']:
				if last_tick['ace'] > 0:
					last_tick['ace'] -= 1
			else:
				last_tick['ace'] = 2

			if located_images['images/victory.png'].result():		
				if not last_tick['end']:
					print("End of game - Won!")
					executor.map(outro, devices)
				this_tick['end'] = True
			
			if located_images['images/defeat.png'].result():
				if not last_tick['end']:
					print("End of game - Lost!")
					executor.map(outro, devices)
				this_tick['end'] = True

			if not this_tick['end']:
				if last_tick['end'] > 0:
					last_tick['end'] -= 1
			else:
				last_tick['end'] = 2
			
