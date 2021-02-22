# Imagine we wanted to to display a --- a^n, where n is an real numbers.
# Ofcouse a*a*a*a*a*...*a would be tedious and combusome.
import math
for i in range(1,21):
	print(i, pow(i,2),sep=' --- ')
