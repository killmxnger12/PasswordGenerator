import modules


# Main function ran as the program has been called
def main():
	# Gives the user the option to decrypt the values or generate a new password
	choice = str(input("Do you wish to generate the password or decrypt one? (gen/dec): "))

	# Prepares the user input for eval
	choice = choice.lower()
	choice = choice.replace(" ", "")

	# Checks if the user input a option that is not available
	if not choice == "gen" and not choice == "dec": 
		print("There is no available option like that...")
		exit()

	# Option to generate the password
	if choice == "gen":
		try:
			# Generates the password
			password = modules.GenPassword()
			print("Password generated successfully!")

			# Encrypts the password values
			encrypted = modules.Encrypt(password)
			print("Password encrypted successfully!")

			# Adds a label to differentiate password from themselves
			label = str(input("What is that password connected to: "))

			# Variable which is used to write to the file
			values_to_write = label + ":\n" + encrypted

			# Write the values to the file
			modules.WriteEncrypted(values_to_write, "passwords.txt")
			print("Password has been successfully written to the file!")
			print("Goodbye!")
			exit()
			

		except ValueError:
			print("There has been an error while running the program...")


	# Option to decrypt the password
	if choice == "dec":
		try:
			# User needs to input the proper encrypted values
			encrypted = input("Paste the encrypted values here: ")
			# Decrypts the values user inputted
			decrypted = modules.Decrypt(encrypted)

			print(decrypted)
		except IndexError:
			print("The encrypted values are not in the correct format...")
			exit()


if __name__ == "__main__":
	main()