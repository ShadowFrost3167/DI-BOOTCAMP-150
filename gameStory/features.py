import os
#to clear cmd
import sys
import time
from levels.level1 import vayihiOr, endedBeforeBegan

def wake():
    gameProgress = "dayOne"
    typeWriter("You wake up in a dark room.")
    typeWriter("OPTIONS: ")
    typeWriter("1. Put on those lights!")
    typeWriter("2. Roll over and return to slumber")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        vayihiOr()
    elif choice == "2":
        wipeClean()
        endedBeforeBegan()
    else:
        wipeClean()
        invalidChoice()
        wake()
#vayihiOr + endedBeforeBegan


def barryFlash(text, speed = .0420):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    time.sleep(.9)
#for gameover() specifically
def typeWriter(text, speed = .06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        #makes typing smooth immidiate
        time.sleep(speed)

    sys.stdout.write("\n")
    #adds new line
    time.sleep(.9)
    #pauses for one sec after lines are printed

run = True
menu = True
play = False
aboutMe = False

LVL = 1
SUAVE = 5
gameProgress = "dayOne" #default start


def invalidChoice():
    typeWriter("Thats not one of the choices!")
    typeWriter("...")
    typeWriter("...")
    typeWriter("PAY")
    typeWriter("ATTENTION")
    
def wipeClean():
    os.system("cls" if os.name == "nt" else "clear")


def gameOver():
    wipeClean()
    print("- - - - - - - - - - -")
    print("- - - - - - - - - - -")
    print("G A M E     O V E R")
    print("- - - - - - - - - - -")
    print("- - - - - - - - - - -")
    time.sleep(2)
    wipeClean()
    barryFlash(" Y O U     D I E D")
    typeWriter("Play again?")
    typeWriter("OPTIONS: ")
    typeWriter("1. Play Again")
    typeWriter("2. Give Up, Be Weak")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        wake()

    elif choice == "2":
        wipeClean()
        barryFlash("Too bad, better luck next time!")
        barryFlash(". . .    . . .    . . .")
        barryFlash(". . .    . . .    . . .")
        barryFlash("window will close now...")
        barryFlash(". . .    . . .    . . .")
        barryFlash(". . .    . . .    . . .")
        exit()


def save():
    #VV--stats--VV
    list = [
        name, 
        str(LVL),
        str(SUAVE),
        gameProgress
    ]

    f = open("load.txt", "w")
    #loads save file or creates new save file

    for item in list:
        f.write(item + "\n")
    f.close()

def invalidChoice():
    typeWriter("Thats not one of the choices!")
    typeWriter("...")
    typeWriter("...")
    typeWriter("PAY")
    typeWriter("ATTENTION")
    
def wipeClean():
    os.system("cls" if os.name == "nt" else "clear")


def gameOver():
    wipeClean()
    print("- - - - - - - - - - -")
    print("- - - - - - - - - - -")
    print("G A M E     O V E R")
    print("- - - - - - - - - - -")
    print("- - - - - - - - - - -")
    time.sleep(2)
    wipeClean()
    barryFlash(" Y O U     D I E D")
    typeWriter("Play again?")
    typeWriter("OPTIONS: ")
    typeWriter("1. Play Again")
    typeWriter("2. Give Up, Be Weak")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        wake()
    elif choice == "2":
        wipeClean()
        barryFlash("Too bad, better luck next time!")
        barryFlash(". . .    . . .    . . .")
        barryFlash(". . .    . . .    . . .")
        barryFlash("window will close now...")
        barryFlash(". . .    . . .    . . .")
        barryFlash(". . .    . . .    . . .")
        exit()


def save():
    #VV--stats--VV
    list = [
        name, 
        str(LVL),
        str(SUAVE),
        gameProgress
    ]

    f = open("load.txt", "w")
    #loads save file or creates new save file

    for item in list:
        f.write(item + "\n")
    f.close()


while run:
    while menu:
        wipeClean()
        print("1. NEW GAME")
        print("2. LOAD GAME")
        print("3. ABOUT GAME")
        print("4. QUIT GAME")

        if aboutMe:
            print("this is a simple text based game created in python for the hackathon project")
            print("please choose to: START, LOAD, OR QUIT with #1, #2, #4")
            aboutMe = False
            choice = ""
            input("> ")

        else:
            choice = input("# ")

        if choice == "1":
            wipeClean()
            name = input("What's your name? ")
            menu = False
            play = True
            save()
            wipeClean()
            
            wake()
            
        elif choice == "2":
            
            f = open("load.txt", "r")
            load_list = f.readlines()

            #save file data
            name = load_list[0][:-1]
            LVL = load_list[1][:-1]
            SUAVE = load_list[2][:-1]
            gameProgress = load_list[3][:-1]

            typeWriter(f"Welcome back {name}! \n Level: {LVL} \n Suave Rating: {SUAVE} \n Day: {gameProgress}")
            typeWriter("game start...")

            if gameProgress == "dayOne":
                wake()
            elif gameProgress == "dayTwo":
                print("THIS IS THE SECOND GAME")

            #transition to game
            menu = False
            play = True
            

        elif choice == "3":
            aboutMe = True
            
        
        elif choice == "4":
            quit()


        else:
            print("HEY BLOCKHEAD! THATS NOT AN OPTION!")

    while play:
        print(f"hello {name}")

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save()

#vvv--starts actual game all functions are just defined above that fit together to make game--vvv 
if __name__ == "__main__":
    wake()

