"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""

#! python3
a = input("The number is:")

a = float(a)

import math
b = a / 8
c = a / 6

b = float(b)
c = float(c)

if b != int(b) and c == int(c):
    print("The number is frue")
else:
    print("The number is not frue")