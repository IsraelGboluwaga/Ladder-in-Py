import random
def one_dice():
	return random.randint(1,6)

def roll():
	print str(one_dice()) + ', ' + str(one_dice())


def inpt():
	userinput = raw_input('Enter y to play again n to quit: \n')
	user_lower = userinput.lower()
	if user_lower == 'y' or user_lower == 'n':
		return user_lower
	elif user_lower != 'y' and user_lower != 'n':
		inpt()

# print inpt()

def dice_simulator():
	roll()
	while inpt() == 'y':
		if 'y':
			roll()
		elif 'n':
			break
		else:
			inpt()
	return 'Bye'


print dice_simulator()