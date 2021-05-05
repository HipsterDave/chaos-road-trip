import os
import time
import sys
import random
import car
import functions
import picklefile
import game

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

def title():
    print('''
    __  __ __   ____   ___   _____     ____   ___    ____  ___        ______  ____   ____  ____  
   /  ]|  |  | /    | /   \ / ___/    |    \ /   \  /    ||   \      |      ||    \ |    ||    \ 
  /  / |  |  ||  o  ||     (   \_     |  D  )     ||  o  ||    \     |      ||  D  ) |  | |  o  )
 /  /  |  _  ||     ||  O  |\__  |    |    /|  O  ||     ||  D  |    |_|  |_||    /  |  | |   _/ 
/   \_ |  |  ||  _  ||     |/  \ |    |    \|     ||  _  ||     |      |  |  |    \  |  | |  |   
\     ||  |  ||  |  ||     |\    |    |  .  \     ||  |  ||     |      |  |  |  .  \ |  | |  |   
 \____||__|__||__|__| \___/  \___|    |__|\_|\___/ |__|__||_____|      |__|  |__|\_||____||__|   

    ''')

def routelist():
    print('''1) East Coast - Key West, FL to Bangor, ME
2) West Coast - Seattle, WA to San Diego, CA
3) North - Bangor, ME to Seattle, WA
4) South - Huntsville, AL to Los Angeles, CA''')

def key_west_1():
	print('''1) Honk
2) Keep driving slow''')

def key_west_2():
	print('''1) Lie - Say that you fell off of a ladder and hit your head.
2) Tell the Truth - Say that an angry bodybuilder smacked you in the face."''')