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
	def __init__(self, speed, off_road, fuel, safety, luxury, size, name):
		self.speed = speed
		self.off_road = off_road
		self.fuel = fuel
		self.safety = safety
		self.luxury = luxury
		self.size = size
		self.name = name

bmw_isetta = car(2, 0, 1, 2, 1, 1, "BMW Isetta")
delorean_dmc12 = car(4, 3, 5, 3, 6, 4, "DeLorean DMC-12")
jeep_wrangler = car(5, 7, 3, 4, 4, 6, "Jeep Wrangler")
toyota_camry = car(5, 4, 7, 6, 4, 5, "Toyota Camry")
m1_abrams = car(3, 10, 3, 7, 3, 10, "M1 Abrams")
bigfoot_5 = car(3, 9, 2, 5, 3, 10, "Bigfoot 5")
toy_car = car(2, 1, 3, 1, 0, 1, "Toy Car")
amphicar_model770 = car(3, 10, 4, 2, 4, 4, "Amphicar Model 770")
# fiat_multipla
horse = car(2, 5, 3, 1, 1, 2, "Horse")
caveman_wheel = car(1, 1, 1, 1, 1, 1, "Caveman Wheel")
model_t = car(3, 3, 1, 2, 3, 4, "Model T")
ford_focus_rs = car(7, 4, 4, 5, 5, 3, "Ford Focus RS")
chevy_camaro = car(8, 4, 4, 4, 5, 4, "Chevy Camaro")

cars = [bmw_isetta, delorean_dmc12, jeep_wrangler, toyota_camry, m1_abrams, bigfoot_5, toy_car,amphicar_model770, horse, caveman_wheel, model_t, ford_focus_rs, chevy_camaro]