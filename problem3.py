#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
a = input("The side1 is:")
b = input("Then side2 is:")
c = input("The hypotenuse is:")

a = int(a)
b = int(b)
c = int(c)

import math

d = a**2
e = b**2
f = c**2

d = float(d)
e = float(e)
f = float(f)

if f == d + e:
    print("They form a pythagorean triple")
else:
    print("They don't from a pythagorean triple")