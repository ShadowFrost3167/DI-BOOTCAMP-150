import os
#to clear cmd
import sys
import time

# name = ""
run = True
menu = True
play = False
aboutMe = False

LVL = 1
SUAVE = 5
gameProgress = "dayOne" #default start

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



def invalidChoice():
    typeWriter("Thats not one of the choices!")
    typeWriter("...")
    typeWriter("...")
    typeWriter("PAY")
    typeWriter("ATTENTION")
    
def wipeClean():
    os.system("cls" if os.name == "nt" else "clear")



def invalidChoice():
    typeWriter("Thats not one of the choices!")
    typeWriter("...")
    typeWriter("...")
    typeWriter("PAY")
    typeWriter("ATTENTION")
    
def wipeClean():
    os.system("cls" if os.name == "nt" else "clear")


# def gameOver():
#     wipeClean()
#     print("- - - - - - - - - - -")
#     print("- - - - - - - - - - -")
#     print("G A M E     O V E R")
#     print("- - - - - - - - - - -")
#     print("- - - - - - - - - - -")
#     time.sleep(2)
#     wipeClean()
#     barryFlash(" Y O U     D I E D")
#     typeWriter("Play again?")
#     typeWriter("OPTIONS: ")
#     typeWriter("1. Play Again")
#     typeWriter("2. Give Up, Be Weak")

#     choice = input("> ")
#     if choice == "1":
#         wipeClean()
#         wake()
#     elif choice == "2":
#         wipeClean()
#         barryFlash("Too bad, better luck next time!")
#         barryFlash(". . .    . . .    . . .")
#         barryFlash(". . .    . . .    . . .")
#         barryFlash("window will close now...")
#         barryFlash(". . .    . . .    . . .")
#         barryFlash(". . .    . . .    . . .")
#         exit()


def save():
    #VV--stats--VV
    list = [
        # name, 
        str(LVL),
        str(SUAVE),
        gameProgress
    ]

    f = open("load.txt", "w")
    #loads save file or creates new save file

    for item in list:
        f.write(item + "\n")
    f.close()
