"""
Introduction to Data Structures, Spring 2022, UMA

Program: ESPN.py
Author: Gimbel
Date Created: 2/28/22
Description: NFL Team Class to track players on individual teams.

"""


class Team():
    """ Team class for producing NFL team objects that provide methods for adding, removing, and listing NFL players from individual teams. """
    
    def __init__(self, name = " "):
        """ Instance variables for Team name and Team implemented as list. """
        self.name = name    # Stores the name of the individual NFL team
        
        self.team = []      # Creates empty list to store players in

    def addPlayer(self, firstName, lastName, position):
        """ Method to add players or append players to dictionary with unique keys of first, last, and position. """
                
        players = {'first': firstName, 'last': lastName, 'position': position}      # Create dictonary for addplayer method
        
        self.team.append(players)       # Append players to dictionary and store them in team list
                
        
    def removePlayer(self, firstName, lastName):        
        
        """ Method that loops over list of dictonary values looking for the keys first and last, then removing the values. """
                       
        for _ in self.team:     # Loop over team list storing items in the _ variable
            
            if _['first'] == firstName and _['last'] == lastName:   # Simple logic checking for values at the key position in loop variable
                
                self.team.remove(_)     # Call list method .remove() to remove the players first and last name
            
    def listPlayers(self):
        """ This method loops over the list of Team players printing out the players name and position using f-string formatting. """
        
        print(f"Current {self.name} players:\t")    # Takes current name of Team object and prints out the current players

        for _ in range(len(self.team)):             # Creates compound index by creating range of values equal to length of the list of Team
            
            print(f"{'':>4}",self.team[_]['first'],self.team[_]['last'] + "," + " " + self.team[_]['position'])
            # F-string formatting to print values 4 spaces to the right. Using the index value of for loop variable to print out the values of each dictionary key in list.

# Note:
#        for n in self.team:
#            for v in n.values():   #This works but needs formatting. I never was able to figure out how to format this properly.
                                    #I realized that the for loop variable could not be indexed to format it with a comma. Because v contained the values after iterating over the list. There would be
                                    #No way to know how many items were in that variable depending on the amount of players added. Also, what you demonstrated was far more pythonic and it works! I worked on this part for
                                    #For three days before you posted the example and finally gave in and looked! Wonderful assignment, learned a ton like paying attention to what I'm looping over and the fact it was a list at this point!
                                
#                if v == ",":
#                    self.team.remove()
#                else:                  
                        
#                    print(v, end=" ")        
        
##############################################################################################################################################################################################################################################        

def main():
    """ A simple test of the class

        A correct program will create output like this:

        Current Patriots players:
             Mac Jones, Quarterback
             Matthew Slater, Special Teams
             Jonnu Smith, Tight End
             N'Keal Harry, Bench Warmer
             Matthew Judon, Linebacker

        Current Patriots players:
             Mac Jones, Quarterback
             Matthew Slater, Special Teams
             Jonnu Smith, Tight End
             Matthew Judon, Linebacker
    """

    patriots = Team('Patriots')
    patriots.addPlayer("Mac", "Jones", "Quarterback")
    patriots.addPlayer("Matthew", "Slater", "Special Teams")
    patriots.addPlayer("Jonnu", "Smith", "Tight End")
    patriots.addPlayer("N'Keal", "Harry", "Bench Warmer")
    patriots.addPlayer("Matthew", "Judon", "Linebacker")    
    patriots.listPlayers()
    print()
    patriots.removePlayer("N'Keal", "Harry")
    patriots.listPlayers()
    

main()


# Amazing project! I used tons of googling and multiple python books on OOP and our textbook. 
# List of sites referenced:
# https://realpython.com/iterate-through-dictionary-python/
# https://python-programs.com/python-iterate-over-dictionary-with-list-values/
# https://www.tutorialstonight.com/python/print-in-python-3.php
# https://stackoverflow.com/questions/64183757/looping-through-list-of-dictionaries
# https://www.youtube.com/watch?v=nghuHvKLhJA
# https://www.youtube.com/watch?v=vTX3IwquFkc
# Books referenced:
# Python Cookbook
# Thinking in Python
# Python Crash Course
# Lean Python 3 The Hard Way