hour = eval(input('Enter hour : '))
hoursAhead = eval(input('How many hours ahead : '))
newHour = (hour+hoursAhead)%12

# Back splash is a special character in python. It an escaping character.
print('New hour :',newHour,'o\'clock')
