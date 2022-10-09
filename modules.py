import random


# Function used to generate a random password of 16 character long
def GenPassword():

	# All the characters the password could contain
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers = "0123456789"
	special_characters = "!#$%&/§@€|łłŁß"

	# Declares the password details
	use_for = lower_case + upper_case + numbers + special_characters
	pass_length = 16

	# Creates the password
	password = "".join(random.sample(use_for, pass_length))

	return password


# Function used to create a key from 5 to 20
def GenKey():
	return random.randint(5, 20) # Modular part #1


# Function used to generate a key value based on the raw key data
def GenKeyValue(key):
	return int((pow(key, 8) + pow(key, 3))/(key * 3)) # Modular part #2


# Function used to encrypt the data using the key value
def Encrypt(data):
	encrypted_values = ""
	key = GenKey()

	encrypted_values += str(key) + ","
	for x in data:
		if x == " ":
			encrypted_values += " "
		else:
			char_value = ord(x) + GenKeyValue(key)
			encrypted_values += str(char_value)
			char_value = ""

	return encrypted_values


# Function used to decrypt the encrypted values using the raw key data
def Decrypt(encrypted):
	decrypted = ""
	counter = 0

	key = encrypted.split(',')[0]
	encrypted_value = encrypted.split(',')[1]

	key_value_len = GetKeyValueLength(key)
	char = ""
	for x in encrypted_value:
		if counter == key_value_len:
			character = chr(int(char) - GenKeyValue(int(key)))
			decrypted += character
			char = ""
			counter = 0
			if x == " ":
				decrypted += " "
			else:
				char += str(x)
				counter += 1
		else:
			char += str(x)
			counter += 1

	character = chr(int(char) - GenKeyValue(int(key)))
	decrypted += character
	char = ""
	counter = 0

	return decrypted


# Almost every key has it's own key value length 
def GetKeyValueLength(key):
	if 5 <= int(key) <= 6:
		return int(5)
	if 7 <= int(key) <= 8:
		return int(6)
	if 9 <= int(key) <= 11:
		return int(7)
	if 12 <= int(key) <= 16:
		return int(8)
	if 17 <= int(key) <= 20:
		return int(9)


# Function used to write values to the text file
def WriteEncrypted(values, filename):
	with open(filename, "a") as file:
		file.write("\n\n")
		file.write(values)
		file.close()