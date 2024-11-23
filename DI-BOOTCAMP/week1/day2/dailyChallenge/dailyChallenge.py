import random 
#for bonus


# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.
# Then, print the first and last characters of the given text.
# The user enters "HelloWorld"
# Then you have to print 
# H
# d

sentence = input(f"write something at least 10 characters long")

if len(sentence) < 10:
    print("string isn't long enough")
elif len(sentence) > 10:
    print("string is too long")
else:
    print("perfect string")
    print(sentence[0])
    print(sentence[-1])

# 3. Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "HelloWorld"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# HelloWorld

for i in range(len(sentence)):
    print(sentence[:i+1])

# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
# Hlrolelwod
if len(sentence) >0:
    gibberish = list(sentence)
    #create list from characters in string

    random.shuffle(gibberish)
    #randomly arranges characters in list of strings

    gobbledegook = ''.join(gibberish)
    #join them together into string called gobbledegook

    print(gobbledegook)