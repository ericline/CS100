"""
Eric Lin
CS 100 2022F Section 009
HW 09, November 10, 2022
"""

import os       # file
import string   # punctuation

# Problem 1

def file_copy(in_file, out_file):

    f = open(in_file, "r")
    o = open(out_file, "w")

    for line in f:
        o.write(line)

    f.close()
    o.close()


file_copy('created_equal.txt', 'copy.txt')
copy_f = open('copy.txt')
print("Problem #1: ")
print(copy_f.read() + "\n")
copy_f.close()

# Problem 2

def file_stats(in_file):

    lines = 0
    words = 0
    characters = 0

    f = open(in_file, "r")

    for line in f:

        characters += len(line)
        
        temp = line.split()
        words += len(temp)
        
        lines += 1

    print("lines " + str(lines))
    print("words " + str(words))
    print("characters " + str(characters) + "\n")

print("Problem #2: ")
file_stats('created_equal.txt')
        
# Problem 3

def repeat_words(in_file, out_file):
    
    f = open(in_file, "r")

    
    
    o = open(out_file, "w")

    for line in f:

        # Create dictionary
        duplicates = {}
        
        words = line.split()
        
        for i in words:
            
            i = i.strip(string.punctuation).lower()
            
            if i in duplicates and duplicates[i] == 1:
                    
                o.write(i + " ")

                duplicates[i] += 1
                
            elif i in duplicates:
                duplicates[i] += 1

            else:
                duplicates[i] = 1

        if len(duplicates) > 0:
            o.write("\n")

    f.close()
    o.close()

repeat_words("catInTheHat.txt", "catRepWords.txt")
repWords = open("catRepWords.txt")
print("Problem #3: ")
print(repWords.read() + "\n")
repWords.close()
