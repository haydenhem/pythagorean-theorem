import math
import numpy as np 
import matplotlib.pyplot as plt


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
    a = input("Type In A: ")
    while not a.isdigit():
        print("That isnt a number! Retype it please!")
        a = input("Type In A: ")
    c = input("Type In c: ")
    while not c.isdigit():
        print("That isnt a number! Retype it please!")
        c = input("Type In c: ")
    c = int(c)
    b = math.sqrt(int(c)**2 - int(a)**2)
    print("B = " + str(b))
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
     c = int(c)
    else:
     print("C = " + "√" + str(c))
     c = math.sqrt(c)
     print("(Decimal) c = " + str(c))
     c = "√" + str(int(a) ** 2 + int(b)**2)
        
a = int(a)
b = int(b)

X = np.array([[0+int(a),0], [0+a,0+b], [0, 0]])
Y = ['red', 'red', 'red']

plt.figure()
plt.scatter(X[:, 0], X[:, 1], s = 170, color = Y[:])
plt.grid()
t1 = plt.Polygon(X[:3,:], color=Y[0])
plt.gca().add_patch(t1)
plt.title("Triangle Grapher")
plt.text(a / 2, b / 2 + b / 8, 'Hypotinus = '+ str(c), fontsize = 10, bbox = dict(facecolor = 'red', alpha = 0.5), rotation=35)
plt.show()
