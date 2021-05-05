import os
import time
import sys
import random
import car
import game
import picklefile
import text
import functions

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

def random_car():
	clear()
	typing("Before we begin your road trip, we need to get you a car! Let's go down to Hal's Car Sales and get one!")
	typing("As you walk inside the building, you realize that you are the 1,000th customer!")
	typing("Hal tells you that since you are his 1,000th customer, you get a random free car!")
	typing("You get...")
	functions.textloading(3, "Choosing Car")
	random_car = random.choice(car.cars)
	typing("...the %s!" % random_car.name)
	picklefile.data.car = random_car
	typing("The %s has a speed of %s, an off-road capability of %s, a fuel capacity of %s, a safety rating of %s, a luxury of %s, and a size of %s." % (picklefile.data.car.name, str(picklefile.data.car.speed), str(picklefile.data.car.off_road), str(picklefile.data.car.fuel), str(picklefile.data.car.safety), str(picklefile.data.car.luxury), str(picklefile.data.car.size)))
	typing("Now, let's start our road trip!")
	time.sleep(1)
	key_west()

def key_west():
	clear()
	picklefile.data.savepoint = 101
	typing("Welcome to Key West, FL! This is where you will begin your road trip.")
	typing("Your first stop is Miami, which is 164 miles away.")
	typing("Let's start our road trip!")
	typing("As you are hopping on and off of small islands, you run into a traffic jam.")
	typing("However, the man in front of you is driving as slow as humanly possible. Do you want to honk at him, or keep quiet?")
	text.key_west_1()
	key_west_1 = ""
	while key_west_1 not in ["1", "2"]:
		key_west_1 = input("> ")
	clear()
	if key_west_1 == "1":
		typing("You honk your horn at the man in front of you.")
		picklefile.data.points -= 100
		typing("The man stops his car and gets out.")
		typing("You see that his muscles are HUGE.")
		typing("You have honked your horn at a professional bodybuilder.")
		typing("The bodybuilder walks over to your car.")
		typing("He knocks at your window and gestures for you to open it.")
		typing("When you open the window, he knocks you in the head.")
		typing("You now have to take a detour to the hospital.")
		time.sleep(1)
		clear()
		typing("You have made it to the Fisherman's Community Hospital in Marathon, FL.")
		typing("Now, the doctor has to ask you some questions.")
		typing("Doctor - How did you get this injury?")
		text.key_west_2()
		key_west_2 = ""
		while key_west_2 not in ["1", "2"]:
			key_west_2 = input("> ")
		clear()
		if key_west_2 == "1":
			typing(picklefile.data.name + " - I fell off a ladder while trying to climb a building.")
			picklefile.data.points -= 100
		elif key_west_2 == "2":
			typing(picklefile.data.name + " - A bodybuilder smacked me in the head.")
			picklefile.data.points += 100
		typing("Doctor - Hmm, that is a very interesting reason. I'm just going to give you an ice-pack and put you on your way!")
		typing("You have received an ice pack!")
		typing("As you walk out of the hospital, you meet the bodybuilder again.")
		typing("Uh oh...")
		typing(picklefile.data.name + " - You can't hurt me! I have an ice pack!")
		typing("You throw the ice pack at the bodybuilder.")
		typing("He gets hit in the head, and he says he will call his lawyer.")
		typing("Hopefully he forgets.")
		typing("You find your %s and ride back on the interstate." % picklefile.data.car.name)
	elif key_west_1 == "2":
		typing("You keep quiet and drive slowly.")
		picklefile.data.points += 100
		typing("This traffic jam takes forever!")
		time.sleep(0.5)
		functions.textloading(3, "Waiting for traffic")
		typing("Whew! That took a long time!")
	typing("As you continue on your journey, ____")

def miami():
	print("yo.")

def orlando():
	print("yo.")

def atlanta():
	print("yo.")

def charlotte():
	print("yo.")

def virginia_beach():
	print("yo.")

def washington_dc():
	print("yo.")

def philadelphia():
	print("yo.")

def new_york():
	print("yo.")

def providence():
	print("yo.")

def boston():
	print("yo.")

def bangor():
	print("yo.")