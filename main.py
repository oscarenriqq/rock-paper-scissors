import random
import time
from os import system

options   = ['rock', 'paper', 'scissor']
attemps_p1 = 3
attemps_p2 = 3

def validateOptions(p1, p2):
    if p1 == p2:
        return 0
    elif p1 == 'rock' and p2 != 'paper':
        return 1
    elif p1 == 'paper' and p2 != 'scissor':
        return 1
    elif p1 == 'scissor' and p2 != 'rock':
        return 1
    else:
        return 2

while True:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    
    choice_p1 = int(input("Rock, paper or scissors? "))
    
    if not (int(choice_p1) >= 1 and int(choice_p1)) <= 3:
        print("Select a valid option")
        input()

        continue
        
    choice_p2 = random.choice(options)

    selectedOption = options[choice_p1 - 1]
    
    result = validateOptions(selectedOption, choice_p2)
    
    print("Rock...")
    time.sleep(.7)
    print("Paper...")
    time.sleep(.7)
    print("Scissors...")
    time.sleep(.7)
    
    print()
    print("PLAYER 1: " + selectedOption + " PLAYER 2: " + choice_p2)
    
    if result == 1:
        attemps_p2 -= 1
        
        if attemps_p2 > 0:
            print ("PLAYER 1 WIN")
        else:
            print("YOU ARE THE CHAMPION!!!")
            break
    elif result == 2:
        attemps_p1 -= 1
        
        if attemps_p1 > 0:
            print ("PLAYER 2 WIN!")
        else:
            print("PLAYER 2 WIN THE PLAY, TRY AGAIN.")
            break
        
    else:
        print("TIE!")
        
    print()
    
    print("Player 1 <3: " + str(attemps_p1))
    print("Player 2 <3: " + str(attemps_p2))
    
    print("--------------------------------")
        
    if attemps_p1 == 0 or attemps_p2 == 0:
        break


