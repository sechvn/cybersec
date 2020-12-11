#   puSticks.py
#   Modified version of Pick-up-Sticks found at www.blocksofcode.com/pick-up-sticks

print("Choose the number of matchsticks (between 5 and 40). The computer will decide who goes first. Remove one, two or three matchsticks from the pile. The contestant who removes the last matchstick loses.", "Rules of the Game")

def PlayAgain():
    answer = input("Would you like to play a game? Y/N ")
    if answer == "Y" or answer == "y":
        newGame()
    else:
        print("Too bad. See ya.")
        exit()
            
def newGame():
    GetNumber()
    OutputSticks()
    WhoGoesFirst()

def GetNumber():
    global numberOfSticks
    numberOfSticks = int(input("Enter a number between 5 and 40 "))
    if(numberOfSticks < 5) or (numberOfSticks > 40):
        print("Invalid Input!")
        GetNumber()

def OutputSticks():
    global numberOfSticks
    sticks = ""
    for i in range(numberOfSticks):
        sticks += "|"
    print(sticks)

def WhoGoesFirst():
    global numberOfSticks
    if (numberOfSticks % 4) == 1:
        print("Player Goes First")
        PlayersTurn()
    else:
        print("Computer Goes First")
        ComputersTurn()

def ComputersTurn():
    global numberOfSticks
    #Insert Code Here
    print("This program needs some work")

def PlayersTurn():
    global numberOfSticks
    #Insert Code Here
    print("This program needs some work")

newGame()
