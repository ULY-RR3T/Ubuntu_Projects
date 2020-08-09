from random import randint
import sys

def printman(life):
    if life == 7:
        print()
        print("______")
    elif life == 6:
        printman(7)
        print("     |")
    elif life == 5:
        printman(6)
        print("     O")
    elif life == 4:
        printman(5)
        print("    /")
    elif life == 3:
        printman(5)
        print("    /|")
    elif life == 2:
        printman(5)
        print("    /|\\")
    elif life == 1:
        printman(2)
        print("    /")
    else:
        printman(2)
        print("    / \\")


def printCurr(guess,word,life):
    if life > 7:
        return 
    printman(life)
    print("\n")

    for i,j in zip(guess,word):
        if i == j:
            print(i,end = " ")
        else:
            print(" ",end = " ")

    print()
    for i in range(len(word)):
        print("_",end = " ")

def check(guess,word):
    isCorrect = True
    for i,j in zip(guess,word):
        if i != j:
            isCorrect = False
    return isCorrect


dic = ["Hi","Bye","Terry","May","Today"]
size = len(dic)
word = dic[randint(0,size)]
guess = []
life = 7

for i in range(size):
    guess.append('*')


printCurr(guess,word,7)
print()

while life != 0 :
    guess = input("Enter Your Guess:").split()
    printCurr(guess,word,life)
    if(check(guess,word)):
        print("You Win!")
        sys.exit()
    life = --life

print("You're Dead!")
