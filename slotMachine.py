import random

#'spin' the row to return a list
def spin_row():
    emojis = ["🐍", "🐳", "🐣", "🦑"]

    return [random.choice(emojis) for _ in range(3) ]
    #for every iteration in range 3 return three emojis 


    # results = []
    # for emoji in range(3):
    # #for each emoji i the list 3 of them
    #     results.append(random.choice(emojis))
    #     #append the random emojis to the results list
    # return results

#display final row
def print_row(row):
    print("===========")
    print("  ".join(row))
    print("===========")


#give tickets based on score
def get_tickets(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🐍":
            return bet * 5
        elif row[0] == "🐳":
            return bet * 7
        elif row[0] == "🐣":
            return bet * 11
        elif row[0] == "🦑":
            return bet * 17
        
    return 0


def playAgain():
    while True:
        print("PLAY AGAIN? ")
        print("1. YES ")
        print("2. NO ")

        #strip wasn't doing the job of removing spaces
        choice = input("> ").strip().replace(" ", "")

        if choice == "1":
            print("\n==============================")
            print("  Welcome to Zlotties!")
            print(" Symbols: 🐍 🐳 🐣 🦑")
            print("==============================")
            return True
        elif choice == "2":
            return False
        else:
            print("\033[38;5;202mDIGITS ONLY!\033[0m")

            

#primary function for slot machine:   

def slotty():
    balance = 100

    #welcome message:
    print("\033[93m==============================\033[0m")
    print("\033[93m  Welcome to Zlotties!\033[0m")
    print("\033[93m Symbols: 🐍 🐳 🐣 🦑\033[0m")
    print("\033[93m==============================\033[0m")

    

    while balance > 0:
        print("")
        print(f"\033[38;5;214mCurrent tokens: {balance}\033[0m")
        #prompt user to enter a bet
        bet = input(f"How much do you want to bet?").strip()

        if not bet.isdigit():
            print("\033[38;5;202mDIGITS ONLY!\033[0m")
            continue

        bet = int(bet)

        if bet > balance:
            print("Not enough tokens!")
            continue

        if bet <= 0:
            print("\033[38;5;202mMust bet more than 0!\033[0m")
            continue

        balance -= bet

        row = spin_row()
        print("\033[93m. . .\033[0m")
        print("\033[93mS P I N N I N G\033[0m")
        print("\033[93m. . .\033[0m")
        print("\033[93m. . .\033[0m")
        print("\033[93mS P I N N I N G . . .\033[0m\n")
        print_row(row)

        payout = get_tickets(row, bet)

        if payout > 0:
            print(f"\033[92mYou won {payout} tokens!\033[0m")
            
        else:
            print(f"\033[91mHaha, you lose\033[0m")

        balance += payout

        #wanted to showe balance for usability
        print(f"\033[38;5;214mCurrent tokens: {balance}\033[0m")
        if not playAgain():
            break

    print(" ")
    print("\033[93m===================================\033[0m")
    print(f"\033[38;5;220mYour current amount of tokens is \033[38;5;220m{balance}\033[0m")
    print("\033[93mThanks for playing Zlotties!\033[0m")
    print("\033[93m===================================\033[0m")
    print("\n\n")
        

if __name__ == '__main__':
    slotty()
    exit()

