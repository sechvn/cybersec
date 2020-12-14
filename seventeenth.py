# Eric Gimbel 12/13/20 Pinewood Derby second program Chap. 6

formatList = [1,2,3,4,5,6,7,8,9,10]	# Create a list of values to format inside my pinewood file.
valueList = [4,6,8,9,5,3,2,7,1,10]	# Created second list to format to float using below for loop.
outfile = open('pinewood.txt', 'w')	# Opened or created pinewood file to write the values to.

for i in range(len(formatList)):	# Iterated over the length of the first list writing and formatting the second list to pinewood file.
	outfile.write("%i %10.2f\n" % (formatList[i], valueList[i]))	#Set to two significant digits so that the float value would have only two zeros.
outfile.close()

def adjustTime(x):	#Function that uses sort function to put the lowest value first in valuelist.
	x.sort()
	x.pop(0)		#Pop function to then take the lowest value at index 0 which is first in valuelist out.
	average = sum(x) / len(x)		#Then declared a variable and took the sum of the values in valuelist with lowest value dropped, then / by length of list.
	return average

outfile = open('pinewood.txt')		#Opened the file back up to read the contents from.

readFile = outfile.read()			#Read contents of file then printed them to user and called the adjustTime average function.

print(readFile,'Your average for pinewood file with lowest time dropped is: \n',adjustTime(valueList))

# For this program I used the same function as the first in Chap 6, which again my tutor did assist in but I wrote myself. 
# I then needed to find a way to write floating point values and format them in a nice way to display to the user before calling
# the function. I used this website to help me do that: http://docs.hyperion-rt.org/en/stable/tutorials/python_writing.html
# It did not work at first because I had initially added a 'b' to 'w' when writing to the file. This caused
# a bytecode error which I fixed by just using 'w'. Then I had to remember to open the file back and read from it
# so that I could use the print function to display the contents of the file and then call the function to drop lowest value
# and average. This program is mostly mine and I figured it out on my own using the book and above site, then using function
# from first Chap 6 project. Can't believe I did it and got it to work.






