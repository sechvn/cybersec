# Eric Gimbel 12/8/20 Derby Racecar 

outfile = open('pinewood.txt', 'w')

onetime = float(input('Please enter the first race time of your Derby race: '))
twotime = float(input('Please enter the second race time of your Derby race: '))
thirdtime = float(input('Please enter the third race time of your Derby race: '))
fourthtime = float(input('Please enter the fourth race time of your Derby race: '))

outfile.write(str(onetime) + '\n')
outfile.write(str(twotime) + '\n')
outfile.write(str(thirdtime) + '\n')
outfile.write(str(fourthtime) + '\n')

outfile.close()
list1 = [onetime, twotime, thirdtime, fourthtime]

def adjustTime(x):
	x.sort()
	x.pop(0)
	average = sum(x) / len(x)
	return average


print(adjustTime(list1))








	





