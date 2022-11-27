from pynput.keyboard import Key, Controller
import pynput.keyboard
keyboard_presser = Controller()

from pynput.mouse import Button
import pynput.keyboard
import time, threading

print("One tap")
def click(x, y, button, pressed):
    if button == Button.left and pressed:
        time.sleep(0.2)
        keyboard_presser.tap('3')
        keyboard_presser.tap('2')
        keyboard_presser.tap('1')

with pynput.mouse.Listener(on_click=click) as listener:
    listener.join()
