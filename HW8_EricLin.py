"""
Eric Lin
CS 100 2022F Section 009
HW 08, November 3, 2022
"""

import random

# Problem 1

def twoWords(length, firstLetter):

    twoWords = []
    
    while True:
        
        lengthWord = input('Enter a 4-letter word please: ')
        if(len(lengthWord) == length):
            break

    while True:
        letterWord = input('Enter a word beginning with '
                           + firstLetter + ' please: ')
        if(letterWord.lower().startswith(firstLetter.lower())):
            break

    twoWords.append(lengthWord)
    twoWords.append(letterWord)

    return twoWords

print("Problem 1")
print(twoWords(4, 'B'))
        
# Problem 2

def twoWordsV2(length, firstLetter):

    twoWords = []

    lengthWord = ''
    letterWord = ''
    
    while len(lengthWord) != length:
        
        lengthWord = input('Enter a 4-letter word please: ')

    while not letterWord.lower().startswith(firstLetter.lower()):
        letterWord = input('Enter a word beginning with '
                           + firstLetter + ' please: ')

    twoWords.append(lengthWord)
    twoWords.append(letterWord)

    return twoWords

print("\nProblem 2")
print(twoWordsV2(4, 'B'))

# Problem 3

def enterNewPassword():

    count = 0
    
    while True:
        password = input("Enter a password: ")

        if(len(password) < 8):
            print("Password cannot be less than 8 characters.")
            continue
        if(len(password) > 15):
            print("Password cannot be more than 15 characters.")
            continue
        if(len(password) >= 8 and len(password) <= 15):
            for char in password:
                if char.isdigit():
                    count += 1
            if(count < 1):
                print("Password must contain at least one digit.")
                continue
                    
            else:
                print("Your password is valid.")
                break

print("\nProblem 3")
enterNewPassword()

# Problem 4

def guessNumber():

    number = random.randrange(101)
    guessNum = 1
    guess = ""

    print("I'm thinking of a number in the range 0-50. "
          + "You have five tries to guess it.")

    while number != guess:

        guess = int(input("Guess " + str(guessNum) + "? "))
        guessNum += 1

        if(guess < number):
            print(str(guess) + " is too low")
            continue

        if(guess > number):
            print(str(guess) + " is too high")
            continue

        if(guess == number):
            print("You are right! I was thinking of " + str(guess) + "!")

            again = input("Play again? (Y/N) ")

            if(again.startswith("Y")):
                
                #Recursive
                guessNumber()
            else:
                break;

print("\nProblem 4")
guessNumber()

