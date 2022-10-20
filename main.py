#!/usr/bin/python
import modules, sys


# Main function ran as the program has been called
def main():
	# Checks if there are multiple values to the command
	if len(sys.argv) > 1:
		# Password generation command part
		if sys.argv[1] == "-gen":
			if sys.argv[2] == "":
				print("There is not a service name the account password is linked to")
				exit()
			try:
				# Generates the password
				password = modules.GenPassword()
				print("Password generated successfully!")

				# Encrypts the password values
				encrypted = modules.Encrypt(password)
				print("Password encrypted successfully!")

				# Variable which is used to write to the file
				values_to_write = sys.argv[2] + ":\n" + encrypted

				# Write the values to the file
				modules.WriteEncrypted(values_to_write, "passwords.txt")
				print("Password has been successfully written to the file!")
				print("Goodbye!")
				exit()
				

			except ValueError:
				print("There has been an error while running the program...")

		# Decryption command part
		if sys.argv[1] == "-dec":
			if sys.argv[2] == "":
				print("There needs to be an encrypted value appended to the command...")
				exit()

			try:
				# User needs to input the proper encrypted values
				encrypted = sys.argv[2]
				# Decrypts the values user inputted
				decrypted = modules.Decrypt(encrypted)

				print("\nThe password is: ", decrypted)
				exit()
			except IndexError:
				print("The encrypted values are not in the correct format...")
				exit()

		# Command usage explanation 
		if modules.AskingHelp(sys.argv[1]):
			print("Usage: python passgen.py [option] [extra_info]")
			print("Option: \n \t -gen \t - Generates a random password and encrypts it")
			print("\t -dec \t - Decrypts the inputted password value provided through [encrypted_values]")
			print("Extra Info: \n \t For option: \n \t \t -gen \t - It requires the input of the service the account password is linked to")
			print("\t\t -dec \t - It requires the input of the encrypted values as they are in the txt file")
	else:
		print("\nThe command is incomplete...")
		exit()


if __name__ == "__main__":
	main()
