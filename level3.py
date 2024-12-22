import sys
from features import wipeClean, typeWriter, invalidChoice, barryFlash, save, run, menu, aboutMe, play, LVL, SUAVE, gameProgress
import time
from slotMachine import slotty

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
        dayThree()

    elif choice == "2":
        wipeClean()
        barryFlash("Too bad, better luck next time!")
        barryFlash(". . .    . . .    . . .")
        barryFlash(". . .    . . .    . . .")
        barryFlash("window will close now...")
        barryFlash(". . .    . . .    . . .")
        barryFlash(". . .    . . .    . . .")
        exit()


def dayThree():
    gameProgress = "dayThree"
    typeWriter("You wake up refreshed and ready for the day!")
    typeWriter("Todays the day you take your interest out for a date!")
    typeWriter("You both love games so you're going to the arcade")
    typeWriter("Try to impress them!")
    typeWriter("OPTIONS: ")
    typeWriter("1. Text your date")
    typeWriter("2. Shower off and head to the arcade")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        rainCheck()
    elif choice == "2":
        wipeClean()
        arcade()
    else:
        wipeClean()
        invalidChoice()
        dayThree()
#vayihiOr + endedBeforeBegan

def rainCheck():
    typeWriter("You texted your interest!")
    typeWriter("But she found you clingy and too needy...")
    typeWriter("She doesn't want to meet with you anymore...")
    typeWriter("Sadness cracks your heart and you die.")
    gameOver()

def arcade():
    typeWriter("You head to the arcade")
    slotty()

dayThree()