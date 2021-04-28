import pickle
import os
import game
import time
import random
import sys

typingspeed = 100

def typing1(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typingspeed)

def typing(text):
    typing1(text + "\n")

class Info():
	def __init__(self):
		self.car = ""
		self.points = ""
		self.highscore = ""
		self.completed_missions = 0
		self.name = ""
		self.cityfrom = ""
		self.statefrom = ""

data = Info()

def clear():
	if sys.platform.startswith("linux"):
		os.system("clear")
	elif sys.platform.startswith("win32"):
		os.system("cls")
	elif sys.platform.startswith("darwin"):
		os.system("clear")

def login_or_signup():
	clear()
	print("1) Login")
	print("2) Signup")
	login_or_signup = ""
	while login_or_signup not in ["1", "2"]:
		login_or_signup = input("> ")
	if login_or_signup == "1":
		login()
	elif login_or_signup == "2":
		signup()

def login():
	clear()
	global file
	global data
	print("Please enter your login information.")
	username = input("Username: ")
	password = input("Password: ")
	file = "{}_{}.pickle".format(username, password)
	if os.path.exists(file):
		data = load()
		game.welcome_back()
	else:
		typing("This account doesn't seem to exist...\n")
		time.sleep(2)
		clear()
		login_or_signup()

def signup():
	clear()
	global username, password, file
	print("Ah! A new player! Please enter your new username and password.")
	username = input("Username: ")
	password = input("Password: ")
	file = "{}_{}.pickle".format(username, password)
	if os.path.exists(file):
		typing("Hmm... This account already exists.\n")
		typing("Try using a different username or password.\n")
		time.sleep(2)
		login_or_signup()
	game.tutorial()

def save():
	global data
	if os.path.exists(file):
		os.remove(file)
	with open(file, 'wb') as f:
		pickle.dump(data, f)

def load():
	with open(file, 'rb') as f:
		data = pickle.load(f)
		return data
	print("Couldn't load saved file!")
	return Data()
