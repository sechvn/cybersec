#Eric Gimbel Final Password Protected

import re    		#Imports the regex library

def main(): 		#Defined the main function for the text using some newlines and tabs then calling my validPass function.
	text = '''
					  PASSWORD PROTECTED
					  ##################

	Your password must be at least:\n\t12 characters long,\n\tcontain at least one number,\n\tone upper case letter,\n\tone lower case letter,\n\tone special character.\n'''
	
	print(text)
	validPass()
	




def validPass():  	# This function uses regex to match the regular expression pattern.
	user = input('Please enter a password: ')
	if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{11,16}$", user):
		print('Valid Password')
	else:
		print('Not a valid Password')
		validPass()  # I call the function again when the user enters a password not matching the required characters and length.
                     # this requires the user to reenter until a valid password is found by the function.

main()

# I used as the main source for the regex expressions this site: https://stackoverflow.com/questions/46582497/python-regex-for-password-validation
# Everything else was me. At first I attempted to try some other ways to do this but they kept failing 
# because I didn't have the regex correct and was attempting another method within the re library. The match
# method worked the best as it was very easy once I got the correct regex to then place the code in some functions
# and design the program to where it will contiue until you enter a correct password then exit.
	
