/*
Example 1
Retrieve user input and display the result on the console.
To print several things at once, separate them by commas. 
Python will automatically insert spaces
*/
name = input('Enter your name')
print('Your Name Is', name)
print('A',1,'B',2)
// Inconvenient
print ('The value of 1+1 is', 1+1, '.') 
// Convenient because we take advantate of the seperator.
// We can set anything to our seperator.
print ('The value of 3+4 is ', 3+4, '.', sep='')  
/* In order to display strings in one line using 
two print statements we need to set the end argument 
to the first print.*/
print('On the first line ', end='')
print('On the same line')

/*
Example 2
The eval function converts the text entered 
by the user into a number. One nice feature 
of this is you can enter expressions, like 
3*12+5, and eval will compute them for you.*/
temp = eval(input('Enter a temperature in Celsius : '))
print('In Fahrenheit, that is ', 9/5*temp+32)

/* Example 3*/
number1 = eval(input('Enter first number : '))
number2 = eval(input('Enter second number : '))
number3 = eval(input('Enter third number : '))
number4 = eval(input('Enter forth number : '))
number5 = eval(input('Enter fifth number : '))
sum = number1+number2+number3+number4+number5
average = sum/5
print('The Average Of Numbers Is ', average)
print('Sum Of All Numbers Is ', sum)


