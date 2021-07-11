from os import system
from time import sleep
system("cls")


def quiz():
    playing = input("Do you want to play? ")
    if playing.upper() != "YES":
        print("Closing Game")
    else: 
        print(" \nOk lets play! \n")

    score = int(0)

#START OF QUIZ

#QUESTION 1
    answer = input("What is A? ")
    if answer.upper() != "A":
        print("Incorrect. Your score is now " + str(score) + "/3. \n")
    else:
        score += 1
        print("Correct! Your score is now " + str(score) + "/3. \n")

#QUESTION 2        
    answer = input("What is B? ")
    if answer.upper() != "B":
        print("Incorrect. Your score is now " + str(score) + "/3. \n")
    else:
        score += 1
        print("Correct! Your score is now " + str(score) + "/3. \n")
#QUESTION 3       
    answer = input("What is C? ")
    if answer.upper() != "C":
        print("Incorrect. Your score is now " + str(score) + "/3. \n")
    else:
        score += 1
        print("Correct! Your score is now " + str(score) + "/3.\n ")

#PASS OR FAIL
    if score > 1:
        print("Congratulations! You passed the test! \n")
    else:
        print("You failed. \n")

#TRY AGAIN QUESION
    try_again = input("Would you like to try again? ")
    if try_again.upper() == "YES":
        quiz() 
    else:
        print("Ok, maybe next time!")
        quit()
        
quiz()