# from gameStory.features import typeWriter, wipeClean, invalidChoice, gameOver, save, SUAVE, LVL, name
# import miniGames.rockPaperScissors as rockPaperScissors
import random
import time   

sentenceList = [
    "Ploni Almoni would like to order an everything bagel with cream cheese toasted and a medium cup of coffee",
    "Harry Linguini would like to order a poppy seed bagel with butter toasted and a small hot chocolate",
    "Lancelot would like to order a medium salad: lettuce, cherry tomatoes, cucumbers, onions, peppers.",
    "Joey Cummings would like to order plain bagel with tuna toasted and a coke on the side.",
    "Chaim Pupik would like to order a blueberry muffin, french onion soup with extra cheese, and a cup of coffee."
]


def workBegin(sentenceList):
    #shuffle sentences so they appear random order to add variety to each day
    random.shuffle(sentenceList)

    #add timer to create more interactivity with user
    start_time = time.time()
    speedTime = 0
    word_count = 0
    score = 0

    print("This section begins work: ")
    print("Type out the sentences to complete the customers order!")

    #iterate through sentenceList
    for order in sentenceList:
        print(order)
        user_input = input("> ").strip()

        #update wc
        word_count += len(order.split())

        #check if input matches order
        if user_input.lower() == order.lower():
            score += 1

            print("\033[92m This is exactly what they wanted! Delicious~ \033[0m")
        
        else:
            print("\033[91m PAY ATTENTION: that's not what they ordered... \033[0m")


    #calculate time passed
    time_passed = time.time() - start_time

    #WPM
    wpm = word_count / (time_passed / 60 )
    #print results
    print(f"\nYou completed {len(sentenceList)} orders in {time_passed:.2f} seconds!")
    print(f"Correct orders: {score}/{len(sentenceList)}")
    print(f"Your average serving speed: {wpm:.2f} words per minute.")

    # Feedback based on performance
    if score == len(sentenceList):
        print("\033[92m Good Job! All the customers were happy! \033[0m")
    elif score >= len(sentenceList) // 2:
        print("\033[93m You tried your best but today was rough... \033[0m")
    else:
        print("\033[91m WHAT HAPPENED?!?! \033[0m")
        

if __name__ == "__main__":
    workBegin(sentenceList)
    exit()

