power = eval(input('Enter power : '))
number = 2**power
numberOfLastDigits = eval(input('Enter number of last digits : '))

lastDigits = number%(pow(10,numberOfLastDigits))
print('Power =',power)
print('Number =',number)
print('Last',numberOfLastDigits,'digit(s)' ,lastDigits)
