from pynput.keyboard import Key, Controller
import time, keyboard, mouse, win32api

keyboard_presser = Controller()

print("Gun")

chat_open = False
enter_pressed = False
clicking = False
while True:
	if keyboard.is_pressed("enter") or keyboard.is_pressed("esc"):
		if not enter_pressed:
			chat_open = not chat_open
		
		enter_pressed = True
	else:
		enter_pressed = False
	
	if chat_open:
		continue
	
	if keyboard.is_pressed("num 4"):
		clicking = True
	elif keyboard.is_pressed("num 5"):
		clicking = False
	
	if clicking and not win32api.GetKeyState(0x02) < 0:
		keyboard_presser.tap("y")
	
	time.sleep(0.04)

