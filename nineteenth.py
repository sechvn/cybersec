# Eric Gimbel 
import random

list1 = [] 		#Create empty list
file1 = open('numbers.txt', 'w') 	#Open a file to write to.

for i in range(1,100): 				#Generate a range of values.
	values = random.randint(1,100) 	#Generate 100 random numbers.
	file1.write(str(values)) 		#Write those random values to the our file.
	file1.write('\n') 				#Remove the newlines from the file.

file1.close() 						#Close the file.


with open('numbers.txt', 'r') as temp_file:  #Use with open to open the file and read while creating temp variable.
	list1 = [list1.rstrip('\n') for list1 in temp_file] #Strip the newline characters from the values in the file then put the values in a list.
	
	
list2 = [int(i) for i in list1]  			#Take all the values from list1 using for loop and cast from str to int

average = sum(list2) / len(list2)  			#Now math can be done using sum to give total of the values and len to give length of list dividing to give average.

print(min(list2), max(list2), sum(list2), average) 	#Display lowest value, highest value, total, and average.


#Josh helped me with this project as well and we actually both learned as went on some of the above code
#using stackoverflow: https://stackoverflow.com/questions/19062574/read-file-into-list-and-strip-newlines
#and: https://stackoverflow.com/questions/3142054/python-add-items-from-txt-file-into-a-list and also
#https://linuxhandbook.com/python-write-list-file/ and https://www.tutorialspoint.com/python/string_rstrip.htm
#I also used some of my previous programs in chapter 6 as well as the our textbook.























