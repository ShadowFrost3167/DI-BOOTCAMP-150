

#created board ↓
goban = [' '] * 9

def display_board():
    # Format each cell to be at least 3 characters wide to keep the grid aligned
    #^3 makes centered but 3 char whide
     print(f"""
    {goban[0]:^3}|{goban[1]:^3}|{goban[2]:^3}
    ---+---+---
    {goban[3]:^3}|{goban[4]:^3}|{goban[5]:^3}
    ---+---+---
    {goban[6]:^3}|{goban[7]:^3}|{goban[8]:^3}
    """)
     #3 quotes to handle multiple lines of f string
    


#player input
def divine_move(shaggy):
    while True:
        try:
            position = int(input(f"Player {shaggy}, played on tile: ")) -1
            if position < 0 or position > 8:
                print("move invalid")
            elif goban[position] != ' ':
                print("HEY someone already played there")
            else:
                goban[position] = shaggy
                break
        except ValueError:
            print("please choose a valid tile")
            #ask to explain this i don't understand the logic


#check if gameover

def check_win():
    trump_card = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]

    #all positible winning combiniations ↑

    for kata in trump_card:
        if goban[kata[0]] == goban[kata[1]] == goban[kata[2]] != ' ':
            return goban[kata[0]]
        
    return None #game still in progress



def play():
    print("You think you can beat me?")
    print(f"-------------------------")
    display_board()

    current_player = 'X'

    for _ in range(9):    # '_' = unused loop
        print(f"Current player: {current_player}")
        divine_move(current_player)
        print("Board after move:")
        display_board()
        winner = check_win()
        if winner:
            print(f"{winner} beat me!")
            display_board()
            print(f"Good job {winner} you're not making joke!")
            
            return
        
        #allow 2 players so not just filling with one letter
        current_player = 'O' if current_player == 'X' else 'X'

    print("Draw") #no winner after 9 turns

play()