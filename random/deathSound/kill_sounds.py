import pyautogui, time

print("Kill sounds")

round_kills = 0
previous_tick_kills = 0

tick_no = 0

while True:
	locations = list(pyautogui.locateAllOnScreen('image.png', confidence=0.95))
	
	location_centers = []
	y_locations = []
	
	for location in locations:
		center = pyautogui.center(location)
		
		if 1300 > center.x or center.x > 1650 or (center.y - 113) % 39 != 0 or center.y in y_locations:
			continue
		
		y_locations.append(center.y)
		location_centers.append(center)
	
	round_kills_adder = len(location_centers) - previous_tick_kills
	
	if round_kills_adder < 0:
		round_kills_adder = 0
	
	round_kills += round_kills_adder
	
	previous_tick_kills = len(location_centers)
	
	tick_no += 1
	
	if tick_no == 16:
		print("kills: ", round_kills)
		if pyautogui.locateOnScreen('image1.png', confidence=0.85, region = (837, 172, 246, 57)):
			print("Round kills is: ", round_kills)
			round_kills = 0
			previous_tick_kills = 0
		tick_no = 0
		
