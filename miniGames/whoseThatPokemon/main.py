import random
print('Welcome to Whose That Pokemon!')
print('You will get a jumbled pokemon')
print('\n set it to rights!')
input('press enter to start!\n')

words = [
    'Pikachu', 
    'Bulbasaur', 
    'Squirtle', 
    'Charmander', 
    'Meowth', 
    "Psyduck", 
    "Jigglypuff", 
    "Nidoran", 
    "Pidgey", 
    "Caterpie", 
    "Mew", 
    "Weedle",
    "Rattata"
      ]
#list of words that will be scrambled

scramWord = ''
scoreBoard = 0

#go through words 1 by 1 and shuffle
for word in range(len(words)):
    scrambled = "".join(random.sample(words[word] , len(words[word])))

    print (f" Unscramble this: {scrambled}")
    guess = input('Type Here: ')

    if guess == words[word]:
        print('CORRECT\n')
        scoreBoard += 1
    else:
        print('WRONG\n')

print(f" \n Your score is: {scoreBoard} PTS!")

if scoreBoard <= len(words)/3:
    print(' You need to read more Pokemon manga...')
else:
    (' Good Game!')
