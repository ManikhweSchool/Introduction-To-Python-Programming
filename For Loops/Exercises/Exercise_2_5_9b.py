fib1 = 1
fib2 = 1
fib = fib1+fib2

numberOfFib = eval(input('Enter Number of Elements In The Sequence : '))
if numberOfFib<=0:
        print('Start Over : Invalid Input.')

elif numberOfFib==1:
        print(fib1)
elif numberOfFib==2:
        print(fib1,fib2,sep=',')
elif numberOfFib==3:
         print(fib1,fib2,fib,sep=',',end='')
else:
        print(fib1,fib2,fib,sep=',',end='')

        for i in range(numberOfFib-3):
                fib1 = fib2
                fib2 = fib
                fib = fib1+fib2
                print(',',fib,sep='',end='')
