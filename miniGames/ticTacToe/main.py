import random
import os
import time

def wipeClean():
    os.system("cls" if os.name == "nt" else "clear")

#making tuple for options because set amount of moves not changing
options = ("rock", "paper", "scissors")

#wanted input to be numeral so created dictionary
numberChoice = {
    "1": "rock",
    "2": "paper",
    "3": "scissors"
}

#player stores clients choice
player =  None
com = random.choice(options)

#not allow gun or other side tools, only things in tuple.
while player not in numberChoice:
    player = input("\n Rock! Paper! Scissors! SHOOT!!\n OPTIONS: \n\n 1. ROCK\n 2. PAPER\n 3. SCISSORS \n>>")

#convert number to choice
playerSelection = numberChoice[player]

print(f"\n Player: {playerSelection}")
print(f" Computer: {com}\n")

if playerSelection == com:
    print("It's a tie!\n")

elif (playerSelection == "rock" and com == "scissors") or \
    (playerSelection == "paper" and com == "rock") or \
    (playerSelection == "scissors" and com == "paper"):
    print("You win")
    
else:
    print("You lose!")

time.sleep(1.5)
wipeClean()

print("GG! We can play again tomorrow!")
time.sleep(1)

exit()



