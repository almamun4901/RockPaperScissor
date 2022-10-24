#Author: MD AL MAMUN
#Date: 10/24/2022
# ROCK PAPER SCISSOR GAME


import random

def game():
    play = True
    userPoint = 0
    computerPoint = 0

    #computer inputs
    computer = ['r','p','s']

    #setting infinite loop
    while play:

        #taking user input
        userInput = input("Enter your r or p or s : ")

        #genrating computer input
        x = random.randint(0,2)
        computerInput = computer[x]

        #setting game quit
        if userInput == 'q':
            play = False
            print("GAME QUIT")
            break

        #checking draw
        elif userInput == computerInput:
            print("draw")
            print('User:', userPoint)
            print("Computer", computerPoint)

        #checking user win
        elif (userInput == 's' and computerInput == 'p') or (userInput == 'p' and computerInput == 'r') or (userInput == 'r' and computerInput == 's'):
            print('User Win')
            userPoint = userPoint + 1
            print('User:', userPoint)
            print("Computer", computerPoint)

        #checking computer win
        else:
            print("computer win")
            computerPoint = computerPoint + 1
            print('User:', userPoint)
            print("Computer", computerPoint)
game()
