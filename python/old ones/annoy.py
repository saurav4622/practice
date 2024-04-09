import random

import pyautogui as pg

import time

animal=('behenkaloda',' madarchod',' dalle')
time.sleep(8)

for i in range(50):
    a=random.choice(animal)
    pg.write("kyun be"+a)
    pg.press("enter")
