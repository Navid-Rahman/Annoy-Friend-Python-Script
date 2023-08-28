# Just run this code, and open WhatsApp Web and the desired person you want to annoy!
# Works on any social media platform, just change the text in the code!

import random

# @python.coder_

import pyautogui as pg

import time

animal=('monkey','donkey','dog')

time.sleep(8)

for i in range(100):
	a=random.choice(animal)
	pg.write("You are a "+a)
	pg.press('enter')