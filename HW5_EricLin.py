"""
Eric Lin
CS 100 2022F Section 009
HW 05, October 6th, 2022
"""

# Problem 1

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "November", "December"]

for i in months:
    if i.startswith("J"):
        print(i)

print("")

# Problem 2

for i in range(99):
    if i % 2 == 0 and i % 5 == 0:
        print(i)

print("")

# Problem 3

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"


for i in horton:
    if(i in vowels):
        print(i)
        


