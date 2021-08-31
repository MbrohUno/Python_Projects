"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
count1 = 1
# assigning the variable for the number of tries.
while count1 <= 3:
    fran_num=random.randint(10,99)
    #the first random variable assignment
    sran_num=random.randint(10,99)
    # the second random variable assignment.
    solution=int(fran_num+sran_num)
    # The addition varibale to the two previous variable.
    print("What is the answer for",fran_num, "+" ,sran_num)
    user_input=int(input("Answer:"))
    # Here this is displayed to request for the user's input
    if user_input==solution:
        print("Correct!! You've gotten " ,count1," correct answer in a row.")
        
        count1+=1
    #This displays information if the user gets the answer correct.
    else:
        print("Incorrect. The expected answer is",solution)
    # if the answer is wront this information is displayed.
        
    
    
