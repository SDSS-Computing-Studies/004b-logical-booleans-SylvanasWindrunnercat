#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
a = input("The number is:")

a = float(a)

if a > 0 and a == int(a):
    print("The number is a positive integer")
else:
    print("The number is not a positive integer")