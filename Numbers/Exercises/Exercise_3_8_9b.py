hour = eval(input('Enter hour : '))
hoursAhead = eval(input('How many hours ahead : '))

if hour<=12 and hour>=1 and hoursAhead<=12 and hoursAhead>=1:
    # Back splash is a special character in python. It an escaping character.
    print('New hour :',(hour+hoursAhead)%12,'o\'clock')
else:
    print('Error : Invalid User Input.')
