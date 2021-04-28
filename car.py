import os
import time
import sys
import random
import game
import functions
import picklefile
import text

typingspeed = 100

def typing1(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typingspeed)

def typing(text):
    typing1(text + "\n")

def clear():
	if sys.platform.startswith("linux"):
		os.system("clear")
	elif sys.platform.startswith("win32"):
		os.system("cls")
	elif sys.platform.startswith("darwin"):
		os.system("clear")

class car():
    def __init__(self, speed, off_road, fuel, safety, luxury, size):
        self.speed = speed
        self.off_road = off_road
        self.fuel = fuel
		self.safety = safety
		self.luxury = luxury
		self.size = size

bmw_isetta = car(2, 0, 1, 2, 1, 1)
delorean_dmc12 = car(4, 3, 5, 3, 6, 4)
jeep_wrangler = car(5, 7, 3, 4, 4, 6)
toyota_camry = car(5, 4, 7, 6, 4, 5)
m1_abrams = car(3, 10, 3, 7, 3, 10)
bigfoot_5 = car(3, 9, 2, 5, 3, 10)
toy_car = car(2, 1, 3, 1, 0, 1)
amphicar_model770 = car(3, 10, 4, 2, 4, 4)
fiat_multipla