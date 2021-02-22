// Print Hello Ten Times.
for i in range(10):
	print('Hello')
	
// Retrieve User Input Ten Times.
for i in range(3):
	num = eval(input('Enter a number: '))
	print ('The square of your number is', num*num)
print('The loop is now done.')

// The Sum Of The First Ten Numbers.
sum = 0
for index in range(10):
	sum += index
print(sum)

// Playing with the range function.
for index in range(5,11):
	print(index,end='',sep=' ')
print()
// Print numbers from 10 to 100 (10, 20, 30,...)
for i in range(10,110,10):
	print(i,end=' ')
print()
// Print numbers from 10, 8, 7,...0
for i in range(10,-2,-2):
	print(i,end=' ')
print()