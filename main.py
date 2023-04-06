import pyautogui
import time
while True:
    time.sleep(0.1)
    pyautogui.typewrite("hello")
    time.sleep(0.1)
    pyautogui.press('enter')