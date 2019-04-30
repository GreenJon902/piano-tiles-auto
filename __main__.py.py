import pyautogui
import keyboard
from time import sleep

#Color of tile
Col = (8, 8, 8)

#middle of tiles
pos1 = (215, 660)
pos2 = (720, 660)
pos3 = (1200, 660)
pos4 = (1680, 660)

print("Put the mouse over the start button.")

sleep(5)

pyautogui.click()

print("Running!")

while True:
	#stop
	try:
		if keyboard.is_pressed('s'):
			break
	except:
		pass
		
	#do click
	if pyautogui.pixelMatchesColor(pos1[0], pos1[1], (Col)):
		pyautogui.click(pos1[0], pos1[1])
		#print(1)
	
	elif pyautogui.pixelMatchesColor(pos2[0], pos2[1], (Col)):
		pyautogui.click(pos2[0], pos2[1])
		#print(2)
	
	elif pyautogui.pixelMatchesColor(pos3[0], pos3[1], (Col)):
		pyautogui.click(pos3[0], pos3[1])
		#print(3)
	
	elif pyautogui.pixelMatchesColor(pos4[0], pos4[1], (Col)):
		pyautogui.click(pos4[0], pos4[1])
		#print(4)


print("Done!")
