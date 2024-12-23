import sys
from features import wipeClean, typeWriter, invalidChoice, barryFlash, save, run, menu, aboutMe, play, LVL, SUAVE, gameProgress
import time
from slotMachine import slotty
from rockPaperScissors import roShamBo
from whosePokemon import pokemonMystery
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
    global gameProgress
    gameProgress = "dayThree"
    global LVL
    LVL += 1
    typeWriter("LVL + 1")
    time.sleep(1.5)
    wipeClean()
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
    typeWriter("When you arrive your interest runs up and hugs you")
    typeWriter("You feel them press up against your body")
    typeWriter("Your stomach flutters and your heart pounds")
    typeWriter("She wants to play Zlotty first")
    typeWriter("You like Ro-Sham-Bo")
    typeWriter("Which will you choose?")
    typeWriter("OPTIONS: ")
    typeWriter("1. Play Zlotty")
    typeWriter("2. Play Rock-Paper-Scissors")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        slotty()
        typeWriter("Since you played what she wanted first you go to play what you wanted now.")
        time.sleep(1.5)
        roShamBo()
        lastGame()

    elif choice == "2":
        wipeClean()
        typeWriter("Your interest looks at you with a peeved face and their jaw clenches")
        typeWriter("You both head over to rock paper scissors together")
        roShamBo()
        typeWriter("Your interest doesn't really like this game... ")
        typeWriter("You bring her to the Zlotty machine quickly to smooth things over")
        time.sleep(1.5)
        slotty()
        lastGame()

    else:
        wipeClean()
        invalidChoice()
        arcade()


def lastGame():
    typeWriter("You've played a couple games and there's 1 game left")
    typeWriter("Whose that pokemon? ")
    typeWriter("You are both big fans")
    pokemonMystery()
    endofGame()


def endofGame():
    typeWriter("You had a great day with your date")
    typeWriter("You go home and go to sleep")
    typeWriter("End of game 1")
    wipeClean()
    save()
    menu
    

