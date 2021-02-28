import pyautogui
import time
import keyboard

time.sleep(8)
f = open("D:/B._programeren/Pyhton/spamApps/bee.txt", "r")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    if keyboard.is_pressed("esc"):
     break