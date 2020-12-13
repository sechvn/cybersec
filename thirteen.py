#Eric Gimbel Tony Gladdis Random Number Guessing Game

import random                 # Import the random module

def randomNumber():			  # Function that creates range of random numbers.
	ranNum = random.randint(1, 100)
	return ranNum

def userinput(message = "Please guess a random number: "):	# Function that passes two arguments with a message that can be changed after calling different function.
	askForNumber = int(input(message))
	return askForNumber

def userNumber(askForNumber, ranNum):	#Function that tests whether random number is too high or too low.
	while askForNumber > ranNum:
		return "Too High"
	if askForNumber < ranNum:
		return "Too Low"
	else:
		return "Congratulations! You guessed correctly."
def main():								#Function that declares boolean values then tests using while loop and allows the game to continue.
	userWins = False
	beginGuess = True

	while userWins or beginGuess:
		ranNum = randomNumber()
		askForNumber = userinput()
		message = userNumber(askForNumber, ranNum)

		while message != "Congratulations":
			print(message)
			askForNumber = userinput("Try Again: ")
			message = userNumber(askForNumber, ranNum)

		print(message)
		userWins = True

main()


# I used this as my main source and reference: https://www.youtube.com/watch?v=xDqkMqjBZiE&t=12s

