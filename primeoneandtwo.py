#Eric Gimbel Prime number generation

def main():
	user = int(input('Please enter a number greater than 1: '))
	for i in range(2, user):
		print("The range of your numbers is: ", i)  	#Generate a range less than what user enters and display.
		continue  										#Continue and go to function to check if number is prime and then display factor if not.
	checkPrime(user)




def checkPrime(prime):  					#Checks if number is prime and ensures users enter number greater than 1.
	if prime < 2:
		print("Your number has to be greater than 2.")
		return

	factors = [(1, prime)]  				#Create set of factors to start.
	x = 2  									#Counter variable.
	while x * x <= prime:  					#Loop until square number is reached.
		if prime % x == 0:   				#Get reminder if 0 append factors to tuple or list (slightly confused on this one. Because of above brackets with ())
			factors.append((x, prime//x))   #Append the square root and divide to get the factors.
		x += 1  							#Increment value.

	if len(factors) > 1:  					#If length of factors is greater than 1 it's not prime print out the factors.
		print(f"{prime} is not a prime number. The number has the following factors: {factors}")
	else:
		print(f"Your {prime} is a prime number")  #Number is prime print the number using format for string)
	
main()       #Call main function.


#I used the following site for the solution to check if the number was or was not
#a prime. One of the issues I had initially was using a for loop with range
#then appending the values to a list and using a different function with simpler
#method of checking if the number entered was a prime or not but when I appended those
#values to the list and called the function it would not work with the % modulus operator
#I think because I allowed the loop to complete the iteration then break out of it and use the 
#int value from the user with the function it was fine. I would have liked to get my original one
#to work but I was able to figure out the main function by myself and then use this to 
#reference and guide me in creating the function that checks whether or not the number 
#entered was a prime. Here is the source: https://realpython.com/python-modulo-operator/
#Then I realized I could have it also print out the factors because of the next program which intitially I didn't.
#Awesome assignment learned a ton and it is now 2:43AM and have to get right back at it. Thank you again for the extra time!