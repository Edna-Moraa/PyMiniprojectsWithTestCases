import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3



print("")
# playerchoice = ("Enter... \n 1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: ")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")    
computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("comp chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == 1 and computer ==3:
    print("🎉 you win")
    
elif player == 2 and computer ==1:
    print("🎉 you win")    

elif player == 3 and computer == 2:
    print("🎉 you win")
elif player == computer:
    print("😊 tie game")    

else:
    print("💻 comp win")        
