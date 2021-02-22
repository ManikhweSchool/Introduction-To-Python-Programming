username = input('Enter Your Name : ')
numberOfTimes = eval(input('Enter number of times : '))

if numberOfTimes>0:
	for i in range(numberOfTimes):
		print(username)
else:
	print('Error : Invalid User Input.')