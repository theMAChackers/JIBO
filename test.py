import pyautogui
import time

time.sleep(5)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX,currentMouseY)