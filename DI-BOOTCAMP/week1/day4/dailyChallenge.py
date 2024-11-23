# Instructions
# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

digit = int(input("I can count by any number! give me a number ANY NUMBER:  "))
length = int(input("How many times do you want to multipy it?"))

timesTable = []

for i in range(1, length +1):
    timesTable.append(digit * i)

print(timesTable)






# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

tourrettes = input(f"write me a word and stutter it")

clearSpeech = ""

for i in range(len(tourrettes)):
    #goes through each index of string given
    if i == 0 or tourrettes[i] != tourrettes[i-1]:
        #check if character is differnt than last one in string
        clearSpeech += tourrettes[i]
        #add character to clearSpeech

print(clearSpeech)

