"""
Eric Lin
CS 100 2022F Section 009
HW 03, September 29th, 2022
"""

import turtle
import math


# Write code that uses turtle graphics to draw an equilateral triangle,
# a square, and a regular pentagon, each with side length 100.

length = 100;

t = turtle.Turtle()
t.width(10)

t.forward(length)
t.left(120)
t.forward(length)
t.left(120)
t.forward(length)
t.left(120)
t.clear()

t.right(90)
t.forward(length)
t.left(90)
t.forward(length)
t.left(90)
t.forward(length)
t.left(90)
t.forward(length)
t.clear()

t.left(72)
t.forward(length)
t.right(72)
t.forward(length)
t.right(72)
t.forward(length)
t.right(72)
t.forward(length)
t.right(72)
t.forward(length)
t.clear()

# Write code that uses turtle graphics to draw four concentric circles of
# radius 50, 100, 150, and 200.

for i in range(50, 200, 50):
    t.right(90)
    t.penup()
    t.forward(i)
    t.right(270)
    t.pendown()
    t.circle(i)
    t.penup()
    t.home()

# Write code that uses the Python math module to compute and print out the
# values of a. 100!, b. log base 2 of 1,000,000, c. GCD of 63 and 49.

print("100! = " + str(math.factorial(100)))
print("log base 2 of 1,000,000 = " + str(math.log2(1000000)))
print("GCD of 63 and 49 = " + str(math.gcd(63, 49)))
