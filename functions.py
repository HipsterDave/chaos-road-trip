import os
import time
import sys
import random
import car
import game
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

def textloading(repeat, text):
	x = repeat
	while x > 0:
		x = x - 1
		print(text + " .")
		time.sleep(1)
		clear()
		print(text + " ..")
		time.sleep(1)
		clear()
		print(text + " ...")
		time.sleep(1)
		clear()

def welcome():
    clear()
    textloading(3, "Booting Up")
    print("CHAOS ROAD TRIP")
    time.sleep(0.5)
    print("Copyright (c) 2021 Cheese, Inc. All rights reserved.")
    time.sleep(0.5)
    print("CHAOS ROAD TRIP is not a registered trademark of Cheese, Inc.")
    time.sleep(0.5)
    print("Revision 12 / Serial number 593027")
    time.sleep(2)
    title_page()

def title_page():
    clear()
    text.title()
    typing("Welcome to CHAOS ROAD TRIP! Would you like to PLAY, HELP, SEE CREDITS, or QUIT?")
    start = ""
    while start not in ["play", "help", "see credits", "quit"]:
        start = input("> ")
    if start == "play":
        picklefile.login_or_signup()
    elif start == "help":
        help()
    elif start == "see credits":
        credits()
    elif start == "quit":
        exit()

def help():
    print("HELP FILLER")
    input("Please press enter to continue.")
    title_page()

def credits():
    typing("This game was created entierly by HIPSTERDAVE and VADERCAT.")
    input("Please press enter to continue.")
    title_page()