#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ("Guile","Blanka","Christine","Carol","Richard","Daniel","Chun-Li")
a = input("Your name is:")

if a == "Guile":
    print("Hello, Guile")
elif a == "Blanka":
    print("Hello, Blanka")
elif a == "Christine":
    print("Hello, Christine")
elif a == "Carol":
    print("Hello, Carol")
elif a == "Richard":
    print("Hello, Richard")
elif a == "Daniel":
    print("Hello, Daniel")
elif a == "Chun-Li":
    print("Hello, Chun-Li")