import os
import time
import sys
import random
import car
import game
import picklefile
import text

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

def random_car():
	clear()
	typing("Before we begin your road trip, we need to get you a car! Let's go down to Hal's Car Sales and get one!")
	typing("As you walk inside the building, you realize that you are the 1,000th customer!")
	typing("Hal tells you that since you are his 1,000th customer, you get a random free car!")
	typing("You get...")
	functions.textloading(3, "Choosing Car")
	random_car = random.choice(car.cars)
	typing("...the %s!" % random_car.name)
	typing("The %s has a speed of %s, an off-road capability of %s, a fuel capacity of %s, a safety rating of %s, a luxury of %s, and a size of %s." % (random_car.name, str(random_car.speed), str(random_car.off_road), str(random_car.fuel), str(random_car.safety), str(random_car.luxury), str(random_car.size)))
	typing("Now, let's start our road trip!")
	seattle()

def seattle():
	print("yo.")