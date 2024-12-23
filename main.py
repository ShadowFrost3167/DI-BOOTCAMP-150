from features import wipeClean, typeWriter, barryFlash, invalidChoice, save, run, menu, aboutMe, play, LVL, SUAVE, gameProgress, name
import time
from level1 import wake, endedBeforeBegan
from level2 import secondMorning
from level3 import dayThree


print("__name__ in main:", __name__)

def save():

    global name
    #VV--stats--VV
    list = [
        name,
        str(LVL),
        str(SUAVE),
        gameProgress
    ]

    print("Saving data from main:", list)
    time.sleep(3)


    with open("load.txt", "w") as f:
    #loads save file or creates new save file

        for item in list:
            if item is not None:
                f.write(item + "\n")
            else:
                print("none main")
                f.write("None\n")

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
        menu = True

    elif choice == "2":
        wipeClean()
        barryFlash("Too bad, better luck next time!")
        barryFlash(". . .    . . .    . . .")
        barryFlash(". . .    . . .    . . .")
        barryFlash("window will close now...")
        barryFlash(". . .    . . .    . . .")
        barryFlash(". . .    . . .    . . .")
        exit()

def runGame():
    global name
    play = False
    run = True
    menu = True
    aboutMe = False
    name = None

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
                print(f"Debug: name entered is {name}")  # Debug print to check name
                save()
                time.sleep(2)
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

                print(f"Debug: loaded name is {name}")  # Debug print to check loaded name


                typeWriter(f"Welcome back player \n Level: {LVL} \n Suave Rating: {SUAVE} \n Day: {gameProgress}")
                typeWriter("game start...")

                if gameProgress == "dayOne":
                    wake()
                elif gameProgress == "dayTwo":
                    secondMorning()
                elif gameProgress == "dayThree":
                    dayThree()

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
        

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                

    #vvv--starts actual game all functions are just defined above that fit together to make game--vvv 
if __name__ == "__main__":
    runGame()

