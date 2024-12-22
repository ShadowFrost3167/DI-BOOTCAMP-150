from features import wipeClean, typeWriter, barryFlash, invalidChoice, save, run, menu, aboutMe, play, LVL, SUAVE, gameProgress
import time
from level1 import wake, endedBeforeBegan
import level2
import level3

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
            menu = False
            play = True
            save()
            wipeClean()

            wake()
            
            
            
        elif choice == "2":
            
            f = open("load.txt", "r")
            load_list = f.readlines()

            #save file data
            
            LVL = load_list[0][:-1]
            SUAVE = load_list[1][:-1]
            gameProgress = load_list[2][:-1]

            typeWriter(f"Welcome back player \n Level: {LVL} \n Suave Rating: {SUAVE} \n Day: {gameProgress}")
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
       

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save()

#vvv--starts actual game all functions are just defined above that fit together to make game--vvv 
if __name__ == "__main__":
    wake()

