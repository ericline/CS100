"""
Eric Lin
CS 100 2020F Section 009
Due Date: 10-20-2022
"""

# Problem 1a

def hasFinalLetter(strList, letters):

    aList = []
    
    for i in strList:
        if i[-1] in letters:
            print(i)
            aList.append(i)
        
    return aList;

# Problem 1b

strList1 = ["UPenn", "NYU", "BU", "NEU", "UMass", "Rutgers"]
strList2 = ["forget", "about", "the", "white", "noise"]
strList3 = ["You", "Have", "To", "Be", "Odd", "To", "Be", "Number", "1"]

letters1 = "cOlLeGeSiWaNtIn"
letters2 = "ITSJUSTCHOCOLATEANDPAJAMAS"
letters3 = "DOnTwOrrYImThESTrOnGEsT1"

test1 = hasFinalLetter(strList1, letters1)
test2 = hasFinalLetter(strList2, letters2)
test3 = hasFinalLetter(strList3, letters3)

passCounter = 0;

print("Test 1: " + str(test1))
if len(test1) == 1:
    print("Passed.")
    passCounter = passCounter + 1
    
print("Test 2: " + str(test2))
if len(test2) == 0:
    print("Passed.")
    passCounter = passCounter + 1
    
print("Test 3: " + str(test3))
if len(test3) == 2:
    print("Passed.")
    passCounter = passCounter + 1

if(passCounter == 3):
    print("All Tests Passed.")

# Problem 2a

def isDivisible(maxInt, twoInts):
    aList = []

    for i in range(1, maxInt):
        if(i % twoInts[0] == 0 and i % twoInts[1] == 0):
            aList.append(i)

    return aList

# Problem 2b

maxInt1 = 125
maxInt2 = 400
maxInt3 = 1000

twoInts1 = (3, 5)
twoInts2 = (4, 7)
twoInts3 = (1001, 1005)

Test1 = isDivisible(maxInt1, twoInts1)
Test2 = isDivisible(maxInt2, twoInts2)
Test3 = isDivisible(maxInt3, twoInts3)

p = 0;

print("Test 1: " + str(Test1))
if len(Test1) == 8:
    print("Passed.")
    p = p + 1
    
print("Test 2: " + str(Test2))
if len(Test2) == 14:
    print("Passed.")
    p = p + 1
    
print("Test 3: " + str(Test3))
if len(Test3) == 0:
    print("Passed.")
    p = p + 1

if(p == 3):
    print("All Tests Passed.")

