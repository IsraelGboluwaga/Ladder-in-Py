import random, string
# The string module can still be used
chars = string.uppercase + string.lowercase + '?*$@!&' + '0123456789'
password = ''

password_length = int(input('Password length? '))
def password_generator(password,length):
	for i in range(length):
		password += random.choice(chars)
	return password
def suggest(password, p_length, s_length):
	for j in range(s_length):
		print password_generator(password,p_length)

no_of_suggestions = input('How many suggestions: ')
suggest(password, password_length, no_of_suggestions)
