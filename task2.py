#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
a = input("The number is:")

import math

a = float(a)

b = math.sqrt(a)

c = math.pow(a,1/0.3)

b = float(b)

c = float(c)

if b == int(b) and c == int(c):
    print("The number is a perfect square and a perfect cube")
elif b == int(b) and c != int(c):
    print("The number is only a perfect square")
elif b != int(b) and c == int(c):
    print("The number is only a perfect cube")
elif b != int(b) and c != int(c):
    print("The number is not a perfect square or a perfect cube")