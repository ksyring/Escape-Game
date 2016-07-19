from sys import exit
#Where I am: 

inventory = []
def addToInventory(item):
	inventory.append(item)
	
def mansion():
	print "The room you enter into is a large front room."
	print "What do you do?"
	print "1. Enter door 1."
	print "2. Enter door 2."
	print "3. Enter door 3."
	
	choice = raw_input("> ")
	if choice == "1":
		kitchen()
	elif choice == "2":
		stairs()
	elif choice == "3":
		closet()
	else:
		print "You need to choose a door."
	
def kitchen():
	print "You walk through the doorway and see a fridge, an oven, and three cupboards."
	print "What do you do?"
	print "1. Open the fridge."
	print "2. Open the oven."
	print "3. Open the cupboards."
	print "4. Leave the kitchen."
	
	choice = raw_input("> ")
	if choice == "1":
		print "The fridge is off and everything is bad inside."
		print "Do you:"
		print "1. Close the fridge and keep looking around the kitchen."
		print "2. Leave the kicten."
		
		choice = raw_input("> ")
		if choice == "1":
			kitchen()
		elif choice == "2":
			start()
		else:
			print "Choose a number, human."
	elif choice == "2":
		print "You open the oven and a small rat runs out at you."
		print "Do you:"
		print "1. Try to catch the rat."
		print "2. Close the oven and keep looking around the kitchen."
		
		choice = raw_input("> ")
		if choice == "1":
			dead("You catch it but it bites you and you die from rabies.")
		elif choice == "2":
			kitchen()
		else: 
			print "Choose a number, human."
	elif choice == "3":
		print "There is a couple of nuts."
		print "Do you:"
		print "1. Keep the nuts."
		print "2. Close the cupboards and keep looking around the kitchen."
		
		choice = raw_input("> ")
		if choice == "1":
			print "They will do you no good."
			kitchen()
		elif choice == "2":
			kitchen()
		else: 
			print "I do not understand, human."
	elif choice == "4":
		start()
	else: 
		print "I do not understand you, human."
		
def stairs():
	print "You decided to take the stairs up, yes?"
	
	choice = raw_input("> ")
	if choice == "yes":
		print "You continue up to the second floor."
		sfloor() #Second floor
	elif choice == "no":
		print "You want to go back out to the main room."
		start()
	else:
		print "Yes or no human, there is no in between."

def sfloor():
	print "You walk up the stairs to find four doors leading into bedrooms."
	print "What door would you like to try first?"
	print "1. Door one."
	print "2. Door two."
	print "3. Door three."
	print "4. Door four."
	print "5. Go back down stairs."
	
	choice = raw_input("> ")
	if choice == "1":
		print "You walk up to the door.\nRattle the handle. \nAnd it opens successfully."
		bedroom1()
	elif choice == "2":
		print "You walk pass the first door and onto the second door. You try to open it but the door is locked."
		sfloor()
	elif choice == "3":
		print "You walk all the way to the third door."
	elif choice == "4":
		print "All the way at the other end of the hallway is the door you choose. It is a steel door with a steel lock. You need a key."
		# need to add in an if statement to see if the "inventory" has a key. Need to make an inventory.
	elif choice == "5":
		print "Heading back down it is."
		mansion()
	else:
		print "You gotta give me a place to work with."

def bedroom1():
	print "Welcome to the first room. Here you find a closet, a bed, and a bat flying around the room."
	print "When you first open the door, the bat sees this opportunity to leave the room."
	print "What would you like to do?"
	print "1. Look inside the closet. \n2. Look around the bed. \n3. Leave this room."
	
	choice = raw_input("> ")
	if choice == "1":
		print "Inside the closet you find a pair of shoes. They do you no good."
	elif choice == "2":
		print "Under the bed, you find a jewlery box. Would you like to open it?"
		choice = raw_input("> ")
		if choice == "yes":
			print "You find a small key. Would you like to add it to your inventory?."
			pickup = raw_input("> ")
			if pickup == "yes":
				addToInventory("small key")
			elif pickup == "no":
				print "You just leave the small key here. Alright."
			else:
				print "Yes or no human."
				
	
def closet():
	print "You open the door of the closet to find three items."
	print "There is one unsharpened sword."
	print "A flashlight, without batteries."
	print "And finally you see the skeleton head of what seems to be a dog."
	print "Do you grab the flashlight, take the skeleton head, take the unsharpened sword or take nothing?"
	
	choice = raw_input("> ")
	if choice == "grab the flashlight":
		print "Well, hopefully you will come across the batteries or else this is useless."
		print "Would you like to grab something else?"
		choice = raw_input("> ")
		if choice == "yes":
			closet()
		elif choice == "no":
			mansion()
		else:
			"Yes or no. C'mon it's not that hard..."
	elif choice == "take the skeleton head":
		print "... What do you plan on doing with that?"
	elif choice == "take the unsharpened sword":
		print "There should be something you can use to sharpen that blade somewhere around here."
	elif choice == "take nothing":
		print "Fair enough."
		mansion()
	else:
		print "Idoit, I am a computer not a mind reader. Type what was given to you."
	
def dead(why):
	print why, "\nGood job!\n"
	
def start():
	print "You enter the mansion."
	print "The room you enter into is a large front room."
	print "As soon as you walk through the door way, the door slams shut behind you."
	print "What do you do?"
	print "1. Try opening the front doors."
	print "2. Enter door 1."
	print "3. Enter door 2."
	print "4. Enter door 3."

	choice = raw_input("> ")
	if choice == "1":		 
		print "They are locked from the outside, you need a key."
		mansion()
	elif choice == "2":
		kitchen()
	elif choice == "3":
		stairs()
	elif choice == "4":
		closet()
	else:
		print "You need to choose a door."
	
start()