power = eval(input('Enter power : '))
number = pow(2,power)
numberOfLastDigits = eval(input('Enter number of last digits : '))

if numberOfLastDigits>0:
    lastDigits = number%(pow(10,numberOfLastDigits))
    print('Power =',power)
    print('Number =',number)
    print('Last',numberOfLastDigits,'digit(s)' ,lastDigits)
else:
    print('Error : Invalid Input.')
