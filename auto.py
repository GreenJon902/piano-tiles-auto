import pyautogui
import keybourd
from time import sleep

#Col of tile
Col = (8, 8, 8)

#middle of tiles
pos1 = (215, 660)
pos2 = (720, 660)
pos3 = (1200, 660)
pos4 = (1680, 660)

print("Put the mouse over the start button.")

sleep(5)

pyautogui.click()

while True:
	#stop part
	try:
		if keybourd.is_pressed("s"):
			break
	except:
		pass
	
	#do click
	if pyautogui.pixelMatchesColor(pos1[0], pos1[1], (Col)):
		payauto.click(pos1[0], pos1[1])
	
	if pyautogui.pixelMatchesColor(pos2[0], pos2[1], (Col)):
		payauto.click(pos2[0], pos2[1])
	
	if pyautogui.pixelMatchesColor(pos3[0], pos3[1], (Col)):
		payauto.click(pos3[0], pos3[1])
	
	if pyautogui.pixelMatchesColor(pos4[0], pos4[1], (Col)):
		payauto.click(pos4[0], pos4[1])

print("Done!")
