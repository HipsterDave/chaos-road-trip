import os
import time
import sys
import random
import car
import functions
import picklefile
import text
import east
import west
import north
import south
from east import random_car

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

def welcome_back():
    print("ja;lksdjflkdsjlksjd;flkjlkalskjdlkjflaksjdl;;sf")

def tutorial():
    clear()
    picklefile.save()
    typing("Welcome to CHAOS ROAD TRIP!")
    typing("Before we begin your journey, what is your name?")
    name_ask = input("> ")
    picklefile.data.name = name_ask
    typing("Also, what city do you live in?")
    city_ask = input("> ")
    picklefile.data.cityfrom = city_ask
    typing("Lastly, what state do you live in? (Please put state initials, such as AL.)")
    state_ask = input("> ")
    picklefile.data.statefrom = state_ask
    picklefile.save()
    typing("Ah, so you are " + picklefile.data.name + " from " + picklefile.data.cityfrom + ", " + picklefile.data.statefrom + "!")
    typing("Nice to meet you!")
    typing("So, before you embark on your trip, let me tell you about what we are going to do.")
    typing("Currently, there are 4 journeys you can take!")
    typing("You can take the west coast route, the east coast route, the north route, and the south route.")
    typing("Each route will have a starting point and an ending point.")
    typing("There will also be little destination cities in the middle of it.")
    typing("Now, let's look at your options!")
    text.routelist()
    typing("Please pick a route.")
    chosen_route = ""
    while chosen_route not in ["1", "2", "3", "4"]:
        chosen_route = input("> ")
    if chosen_route == "1":
        random_car()