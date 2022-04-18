import pyautogui as pg
import time

time.sleep(5)

for i in range(50):
    pg.write(" Hi, hw r u??")
    time.sleep(0.5)
    pg.press("Enter")