#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
a = input("The bigger number(positive interger) is:")
b = input("The smaller number(positive interger) is:")

a = float(a)
b = float(b)

import math

c = a / b

c = float(c)

if c == int(c):
    print("The smaller number is the factor of bigger number")
else:
    print("The smaller number is not the factor of bigger number")