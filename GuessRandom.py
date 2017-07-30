'''
Todo
The program will first randomly generate a number unknown to the user. The user needs to guess what that number is.
If the user's guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low)
If the user guesses correctly, a positive indication should appear

By: IsraelGboluwaga on 21/07/2017
'''

from random import randint

def genRandom():
#Gets a random integer.
# You can indicate what range of numbers you need. If you dont want integers, dont import randint [alone]
	return randint(1, 10)

def user_input():
#To check and validate user input to be between 1 and 10
	guess = input("Guess a number from 1 to 10:\n")
	num = int(guess)
	if num <= 10 and num > 0:
		return num
	else:
		return user_input()

def check():
#checks if the answer is right or wrong
	rand = genRandom()
	num = int(user_input())
	diff = num - rand
	if num == rand:
		print "You got it right"
	elif diff > 0:
		print "Your answer is too high. The difference is %d, the answer is %d" % (diff, rand)
	elif diff < 0:
		print "Your answer is too low. The difference is %d, the answer is %d" % (abs(diff), rand)
	return play_again()



def play_again():
	resp = raw_input("Wanna try again? Enter Y/N \n")
	if resp.lower() == "y":
		check()
	elif resp.lower() == "n":
		print "Bye"
	else:
		play_again()
	# return "Thanks for using!!!"


# check()
# print user_input()
def game():
	print "Welcome to EaziGuess!"
	check()
	print "Thanks Yo!!!"

game()
