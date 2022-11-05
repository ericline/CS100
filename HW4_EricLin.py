"""
Eric Lin
CS 100 2020F Section 009
HW 04, October 4th, 2022
"""

import turtle

# Problem 1

a = 3
b = 4
c = 5

if(a < b):
    print("OK")

if(c < b):
    print("OK")

if(a + b == c):
    print("OK")

if(a**2 + b**2 == c**2):
    print("OK")

# Problem 2

if(a < b):
    print("OK")
else:
    print("NOT OK")

if(c < b):
    print("OK")
else:
    print("NOT OK")

if(a + b == c):
    print("OK")
else:
    print("NOT OK")

if(a**2 + b**2 == c**2):
    print("OK")
else:
    print("NOT OK")

# Problem 3

draw = turtle.Turtle()

color = input("What color? ")
width = int(input("What line width? "))
length = int(input("What line length? "))
shape = input("line, triangle, or square? ")

if(shape == "line"):
    draw.color(color)
    draw.width(width)
    draw.forward(length)
    
elif(shape == "triangle"):
    draw.color(color)
    draw.width(width)
    draw.left(60)
    draw.forward(length)
    draw.right(120)
    draw.forward(length)
    draw.right(120)
    draw.forward(length)

elif(shape == "square"):
    draw.color(color)
    draw.width(width)
    draw.forward(length)
    draw.left(90)
    draw.forward(length)
    draw.left(90)
    draw.forward(length)
    draw.left(90)
    draw.forward(length)
    draw.left(90)

else:
    print("That is not an option.")
