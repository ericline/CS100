"""
Eric Lin
CS 100 2022F Section 009
HW 02, September 22th, 2022
"""

# Question 1

grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']

A = grades.count('A')
B = grades.count('B')
C = grades.count('C')
D = grades.count('D')
F = grades.count('F')
frequency = [A, B, C, D, F]
print(frequency)

# Question 2a

dog_breeds = ["collie", "sheepdog", "Chow", "Chihuahua"]

# Question 2b

herding_dogs = dog_breeds[0:2]

# Question 2c

tiny_dogs = dog_breeds[3]

# Question 2d

if "Persian" in dog_breeds:
    print(True)
else:
    print(False)
