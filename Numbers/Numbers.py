# Generating a random integer between 1 and 10 inclusively.
from random import randint
x = randint(1,10)
print('A random number between 1 and 10: ', x)
print()

# The following methods do not require importing the math module.
print(abs(-4.3))
print(round(3.336, 2))
print(round(345.2, -1))

# Trigonometry Functions
from math import sin, pi
print('Pi is roughly', pi)
print('sin(90) =', sin(90))


# Getting help on the math module type the following lines.
import math
dir(math)
# To Get Help On A Specific Method Type The Following.
help(math.pow)

from math import* # Imports everything from the math module.
