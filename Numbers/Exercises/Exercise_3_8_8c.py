totalTime = eval(input('Enter number of seconds : '))
if totalTime>0:
    minutes = totalTime//60
    seconds = totalTime%60

    print(minutes,'minute(s)')
    print(seconds,'second(s)',)
else:
    print(totalTime,'is an invalid number of seconds.')
