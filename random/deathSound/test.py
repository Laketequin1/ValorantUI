import pyscreeze, time
from PIL import ImageGrab

while True:
    start = time.time()

    pic = ImageGrab.grab(bbox = (0, 0, 50, 50))

    found = pyscreeze.locate('test.png', pic, confidence=0.95)
    found = pyscreeze.locate('test.png', pic, confidence=0.95)
    found = pyscreeze.locate('test.png', pic, confidence=0.95)
    found = pyscreeze.locate('test.png', pic, confidence=0.95)
    found = pyscreeze.locate('test.png', pic, confidence=0.95)

    print(round(time.time() - start, 2))