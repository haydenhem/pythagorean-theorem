import math


print("a^2 + b^2 = c^2 calculator")
a = ""
b = ""
c = ""

ask = input("What variable do you want to solve for? (A/B/C) ")
if any(ask.lower() == f for f in ["a", "1"]):
    b = input("Type In B: ")
    while not b.isdigit():
        print("That isnt a number! Retype it please!")
        b = input("Type In B: ")
    b = int(b)
    c = input("Type In c: ")
    while not c.isdigit():
        print("That isnt a number! Retype it please!")
        c = input("Type In c: ")
    c = int(c)
    a = math.sqrt(c**2 - b**2) 
    print("A = " + str(a))
if any(ask.lower() == f for f in ["b", "2"]):
    b = input("Type In A: ")
    while not b.isdigit():
        print("That isnt a number! Retype it please!")
        b = input("Type In A: ")
    c = input("Type In c: ")
    while not c.isdigit():
        print("That isnt a number! Retype it please!")
        c = input("Type In c: ")
    b = math.sqrt(int(c) ** 2 - int(a) ** 2)
    print("B = " + b)
if any(ask.lower() == f for f in ["c", "3"]):
    a = input("Type In A: ")
    while not a.isdigit():
        print("That isnt a number! Retype it please!")
        a = input("Type In A: ")
    b = input("Type In B: ")
    while not b.isdigit():
        print("That isnt a number! Retype it please!")
        b = input("Type In B: ")
    c = int(a) ** 2 + int(b) ** 2
    if math.sqrt(c).is_integer():
     c = int(math.sqrt(c))
     print("C^2 = "+str(c))
    else:
     print("C = " + "√" + str(c))
