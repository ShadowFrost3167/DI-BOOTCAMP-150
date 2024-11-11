# Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

print('Hello world\n'*4)

############################################################################################################

# Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

dal_mation = 99
cru_ella = int(dal_mation) ** 3
result = int(cru_ella * 8)
print(f"the results are in! your number issssss: {result}")
############################################################################################################

# Exercise 3 : What is the output ?
# Instructions
# Predict the output of the following code snippets:

# >>> 5 < 3
    #false
# >>> 3 == 3
    #true
# >>> 3 == "3"
    #false
# >>> "3" > 3
    #ERROR, bc the grater than or less than is comparing you can't compare string and int
# >>> "Hello" == "hello"
    #false

############################################################################################################

# 🌟 Exercise 4 : Your computer brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = 'Lenovo'
print(f"I have a {computer_brand} computer")

############################################################################################################

# 🌟 Exercise 5 : Your information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code


name = 'Ariel'
age = 30
shoe_size = 8
info = "My name is {} and I am {} years old. I need Air Force Ones in a size {}".format(name, age, shoe_size)
print(info)

#since i did an f statement for the above exercise iw anted to use .format for this one

############################################################################################################

# 🌟 Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.
a = 11
b = 7

if a>b:
    print('Hello World')

############################################################################################################

# Exercise 7 : Odd or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

user_oddity = input('Gimme a number! Any number!!!')
if int(user_oddity) % 2 == 0:
    print("that's an EVEN number!")
else:
    print("That number is odd")

############################################################################################################

# 🌟 Exercise 8 : What’s your name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

my_name = 'Ariel'
your_name = input('what is your name?  ')

if your_name == my_name:
    print('omegersh! me too! xoxoxo')
elif your_name == 'ariel':
    print('omegersh! me too! xoxoxo')
else:
    breakpoint

    #only included the lowercase version of mine because sometimes i know for inputs i never capitalize, is there a way to disreguard the caps or lower of inputs?

############################################################################################################

# 🌟 Exercise 9 : Tall enough to ride a roller coaster
# Instructions
# Write code that will ask the user for their height in centimeters.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

height = input('How tall are you in cm?    ')

if int(height) > 145:
    print('Yay! your tall enough to ride this ride! good job!')
else:
    print('Lay off the coffee! You need to grow a bit more and ride this ride.')