from gamestory.features import typeWriter, wipeClean, invalidChoice, gameOver, save, SUAVE, LVL, name

from level2 import dayTwo

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

def grabCat():
    typeWriter("You reach down with both hands and grab her.")
    typeWriter("Your fingers sink into the fluffy thick fur")
    typeWriter("Her wailed MEOW of protest echos through the room as you trot back to your bed")
    typeWriter("You settle into the bed with her purring next to you")
    typeWriter("Losing yourself in her warmth you drift off until the morning sufficiently heated")
    dayTwo()
#day2Tranz
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
#feedCat + grabCat

def feedCat():
    typeWriter("you shuffle over to her food, taking care of where you step on the bare creaky floor")
    typeWriter("as you reach down to open the container with cat-food your back twinges")
    typeWriter("you ignore it and press on")
    typeWriter("your back breaks, and you're paralyzed")
    typeWriter("no one comes to your assistance on the drafty cold floor")
    typeWriter("you die of exposure, shouldn't have been so soft eh?")
    typeWriter("try again")
    gameOver()
#GO

def backToBed():
    print("You go back to your room and see the cat curled up in bed waiting for your return")
    print("You settle into the blankets and relax into the warm comfort of being dry with a warm body next to you")
    print("You drift off until the morning")
    dayTwo()
#day2Tranz