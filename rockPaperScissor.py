import random
from random import randint
def game():
    play = True
    computer = ['r','p','s']
    while play:
        userInput = input("Enter your r or p or s : ")
        x = random.randint(0,2)
        computerInput = computer[x]
        if userInput == 'q':
            play = False
            print("GAME QUIT")
            break
        elif userInput == computerInput:
            print("draw")

        elif (userInput == 's' and computerInput == 'p') or (userInput == 'p' and computerInput == 'r') or (userInput == 'r' and computerInput == 's'):
            print('User Win')

        else:
            print("computer win")

game()
