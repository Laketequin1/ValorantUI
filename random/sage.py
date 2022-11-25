from pynput.keyboard import Key, Controller
keyboard_presser = Controller()

from pynput.mouse import Button, Controller, Listener
mouse_presser = Controller()

import time, keyboard, mouse, win32api

print("Sage")

clicking = False
chat_open = False
enter_pressed = False ############ chamber, sounds on kill, hover gun

while True:
	if keyboard.is_pressed("enter") or keyboard.is_pressed("esc"):
		if not enter_pressed:
			chat_open = not chat_open
		
		enter_pressed = True
	else:
		enter_pressed = False
	
	if chat_open:
		continue
	
	if keyboard.is_pressed("num 7"):
		if not clicking:
			keyboard_presser.tap("x")
			time.sleep(0.1)
		clicking = True
	elif keyboard.is_pressed("num 8") or keyboard.is_pressed("1") or keyboard.is_pressed("2") or keyboard.is_pressed("3") or keyboard.is_pressed("c") or win32api.GetKeyState(0x06) < 0:
		clicking = False
	
	if win32api.GetKeyState(0x01) < 0 and clicking:
		clicking = False
		for x in range(80):
			mouse_presser.click(Button.left) # Click
			time.sleep(0.01)
	
	if clicking:
		mouse_presser.click(Button.x1)
		keyboard_presser.tap("x")
	
	time.sleep(0.015)
