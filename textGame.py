import os
#to clear cmd
import sys
import time
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

def vayihiOr():
    typeWriter("ILLUMINATION!")
    typeWriter("You can now see the furniture in your room and the posters on your wall, your cat is sleeping on your desk")
    typeWriter("OPTIONS: ")
    typeWriter("1. Go to your cat")
    typeWriter("2. Go to bathroom")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        catto()
    elif choice == "2":
        wipeClean()
        tinkle()
    else:
        wipeClean()
        invalidChoice()
        vayihiOr()
#catto + tinkle

def endedBeforeBegan():
    typeWriter("you turn over and sink your face deeper in the pillow")
    typeWriter("it's so peaceful and calm, you fall asleep")
    typeWriter("you suffocate on your pillow and die")
    typeWriter("guess you shouldn't have been so lazy")
    typeWriter("try again")
    gameOver()
#GO

def catto():
    typeWriter("The room is drafty from poor insulation")
    typeWriter("The drafty room makes you chatter and shiver violently as you approach her")
    typeWriter("If only you had a source of heat...")
    typeWriter("OPTIONS: ")
    typeWriter("1. Grab her!")
    typeWriter("2. Pet her~")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        grabCat()
    elif choice == "2":
        wipeClean()
        petCat()
    else:
        wipeClean()
        invalidChoice()
        catto()
#grabCat + petCat 

def grabCat():
    typeWriter("You reach down with both hands and grab her.")
    typeWriter("Your fingers sink into the fluffy thick fur")
    typeWriter("Her wailed MEOW of protest echos through the room as you trot back to your bed")
    typeWriter("You settle into the bed with her purring next to you")
    typeWriter("Losing yourself in her warmth you drift off until the morning sufficiently heated")
    dayTwo()

def petCat():
    typeWriter("As your fingers sink into the soft thick fur she purrs")
    typeWriter("She creaks an eye open and yawns before standing an all fours and stretching")
    typeWriter("She stretches up an down and all around as you comb her fur with your fingers")
    typeWriter("She jumps to the floor and starts to sniff her empty bowl")
    typeWriter("She looks peckish but it's so late...")
    typeWriter("OPTIONS: ")
    typeWriter("1. Give some food to the poor thing! She's skin and bone...")
    typeWriter("2. Grab her! She can eat in the morrow!")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        feedCat()
    elif choice == "2":
        wipeClean()
        typeWriter("+1 SUAVE PTS") 
        global SUAVE  #reference the global SUAVE
        SUAVE += 1  # Increase SUAVE by 1
        save()  # Continue with the game as normal
        grabCat()

    else:
        wipeClean()
        invalidChoice()
        petCat()

def feedCat():
    typeWriter("you shuffle over to her food, taking care of where you step on the bare creaky floor")
    typeWriter("as you reach down to open the container with cat-food your back twinges")
    typeWriter("you ignore it and press on")
    typeWriter("your back breaks, and you're paralyzed")
    typeWriter("no one comes to your assistance on the drafty cold floor")
    typeWriter("you die of exposure, shouldn't have been so soft eh?")
    typeWriter("try again")
    gameOver()

def tinkle():
    print("You go to your bathroom and relieve yourself")
    print("OPTIONS: ")
    print("1. Go directly back to your room, it's too cold to wash atm")
    print("2. Ewwwwwww... Wash your hands!")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        backToBed()
    elif choice == "2":
        wipeClean()
        pneumonia()

    else:
        wipeClean()
        invalidChoice()
        tinkle()

#backToBed + pneumonia
def backToBed():
    print("You go back to your room and see the cat curled up in bed waiting for your return")
    print("You settle into the blankets and relax into the warm comfort of being dry with a warm body next to you")
    print("You drift off until the morning")
    dayTwo()

def pneumonia():
    print("As the icey water runs over your hands they sting in agony")
    print("While you suds your hands with soap the sensitivity and chill is almost too much")
    print("You go to dry your hands only to realize: ... ... ... your roommate hasn't left any dry towels in the bathroom")
    print("You make you way back to the room with cold hands AND feet since some water also fell on your sock laden feet")
    print("You shiver as you settle into bed and even though the cat attempts to warm you in an effort to save you from yourself")
    print(f"The damage is already done {name}, it's over... ")
    print("You died of pneumonia and overexposure to cold weather...")
    gameOver()
#youDie
def dayTwo():
    global gameProgress
    gameProgress = "dayTwo"
    global LVL
    LVL += 1
    save()
    wipeClean()
    typeWriter(". . . ")
    typeWriter(". . . ")
    typeWriter("S A V I N G ")
    typeWriter(". . . ")
    typeWriter(". . . ")
    typeWriter("S A V I N G ")
    typeWriter(". . . ")
    typeWriter(". . . ")
    wipeClean()
    typeWriter("would you like to continue here? all progress will be saved automatically each day")
    typeWriter("OPTIONS: ")
    typeWriter("1. QUIT AND COME BACK TO SAVE FILE LATER")
    typeWriter("2. CONTINUE")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        exit()
    elif choice == "2":
        secondMorning()

    else:
        wipeClean()
        invalidChoice()
        dayTwo()
#checkpoint
def secondMorning():
    typeWriter("The sun shines through the dust caked window to your left")
    typeWriter("You look at the clock above the mantle and notice the time")
    typeWriter("   9 A. M. ?!?!?!")
    typeWriter("You usually leave at   8 : 30 ")
    typeWriter("OPTIONS: ")
    typeWriter("1. Hurry to the cafe for work!")
    typeWriter("2. Message and say you'll be late")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        cafeEnter()
    elif choice == "2":
        wipeClean()
        lateWorker()
    else:
        wipeClean()
        invalidChoice()
        secondMorning()
#begin day2

def startWork():
    pass


def cafeEnter():
    typeWriter("You rush out your door after slipping on your jeans in record time")
    typeWriter("Your rusted bike on the porch creaks and groans as you pedal as fast as possible")
    typeWriter("You reach to work and enter before any customers have arrived")
    typeWriter("SUAVE +2")
    global SUAVE
    SUAVE += 2
    save()
    typeWriter("Your coworker Ephram who your close to challenges you to your morning competition")
    typeWriter("OPTIONS: ")
    typeWriter("1. Play Rock Paper Scissors?")
    typeWriter("2. Decline, you're too busy! People might be there any moment.")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        #rockPaperScissors()
    elif choice == "2":
        wipeClean()
        startWork()
    else:
        wipeClean()
        invalidChoice()
        cafeEnter()

def lateWorker():
    typeWriter("There's no way you'll make it in time")
    typeWriter("You don't want to look slovenly on top of be tardy...")
    typeWriter("You take out your phone and message your boss informing him you'll be a bit late")
    typeWriter("SUAVE -1")
    global SUAVE
    SUAVE -= 1
    save()
    typeWriter("You trudge downstairs and eat breakfast what will you eat?")
    typeWriter("OPTIONS: ")
    typeWriter("1. Cofee and blueberry muffin, great for a long day of work!")
    typeWriter("2. Scrambled eggs with OJ, classic breakfast.")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        carbBreaky()
    elif choice == "2":
        wipeClean()
        proteinBreaky()
    else:
        wipeClean()
        invalidChoice()
        lateWorker()

def carbBreaky():
    pass

def proteinBreaky():
    pass

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
                secondMorning()

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

