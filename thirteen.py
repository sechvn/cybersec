import random

def randomNumber():
	ranNum = random.randint(1, 100)
	return ranNum

def userinput(message = "Please guess a random number: "):
	askForNumber = int(input(message))
	return askForNumber

def userNumber(askForNumber, ranNum):
	if askForNumber > ranNum:
		return "Too high"
	elif askForNumber < ranNum:
		return "Too low"
	else:
		return "Congratulations! You guessed correctly."

def main():
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




