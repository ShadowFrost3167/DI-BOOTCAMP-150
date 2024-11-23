# 🌟 Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.


my_fav_numbers = {3, 7, 11, 13, 17, 23, 31, 613}

my_fav_numbers.add(773)
my_fav_numbers.add(797)

print(my_fav_numbers)

my_fav_numbers.remove(31)
print(my_fav_numbers)

friend_fav_numbers = {1, 2}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)


################################################################################################

# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?          NO



################################################################################################

# 🌟 Exercise 3: List
# Instructions
# Using this list 

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove “Banana” from the list.
basket.pop(0)
# Remove “Blueberries” from the list.
basket.pop(-1)
# Add “Kiwi” to the end of the list.
basket.append("Kiwi")
# Add “Apples” to the beginning of the list.
basket.insert(0, "Apples")
# Count how many apples are in the basket.
johnny_appleseed = basket.count("Apples")
print(johnny_appleseed)
# Empty the basket.
basket.clear()
# Print(basket)
print(basket)

################################################################################################

# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float? a float has a decimal point. 
# Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

floaty_int_list = []
start = 1
while start <= 5:
    floaty_int_list.append(round(start, 1))
    start += .5
print(floaty_int_list)

# Can you think of another way to generate a sequence of floats?

another_way = [round(1+.5 *i, 1) for i in range(17)]
print(another_way)


################################################################################################

# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.

# for roaring in range(1, 21):
#     print(roaring)


# commented out because i could include the next part within
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for roaring in range(1, 21):
    if roaring % 2 == 0:
        print(roaring)


################################################################################################

# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

my_name = "ariel"
user_name = input("What's your name? IT BETTER BE THE SAME AS MINE!").strip().lower()

if my_name == user_name:
    print(f"{user_name.capitalize()}, good strong name, just like mine :)")

while user_name != my_name:
    user_name = input("that's not the same as me! try again!").strip().lower()

    if user_name == my_name:
        print(f"{user_name.capitalize()}, good strong name, just like mine :)")
        break


################################################################################################

# 🌟 Exercise 7: Favorite fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".

favourite_fruits_list = input("please input several of your favourite fruits with a space in between, ex: tomato orange shezek")
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
wish_list_fruit = favourite_fruits_list.split()
print(wish_list_fruit)
# Now that we have a list of fruits, ask the user to input a name of any fruit.

wish_upon_a_spam_sandwhich = input("which single fruit do you want to eat most right now?")
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.

if wish_upon_a_spam_sandwhich in wish_list_fruit:
    print("You chose one of your favorite fruits! Enjoy!")


# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

if wish_upon_a_spam_sandwhich not in wish_list_fruit:
    print("You chose a new fruit. I hope you enjoy")

################################################################################################

# Exercise 8: Who ordered a pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.

pizza_toppings = []

pie = 10

while True:
    #while true starts infinite loop will keep asking while ture the break after quit being entered is the only way to end the question loop
    user_wishes = input("what do you want on your pizza? list each topping in this prompt box by themsleves type quit in a message box when you're happy")

    if user_wishes.lower() == "quit":
        break

    else:
        pizza_toppings.extend(user_wishes.split())
    #add inputs to list

        print("so far on your pizza you want: ",", ".join(pizza_toppings))
    #print inputs with comma in between


# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

print("The cost of pies with us is 10 for a plain and 2.5 extra per topping")

topping_gouge = len(pizza_toppings)
#sets a variable to length of toppings
black_mail = pie + (topping_gouge * 2.5)
print("your total is: ", black_mail)

################################################################################################

# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# age = i
# wrote this initially to build the structure for myself visually of what i was doing

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.


final_price = 0
family_age_group = []

while True:
    i = input("how old are your family members? input each age digitally until you're finished then type 'end' to finish      ")

    if i.lower() == 'end':
        break

    try:
        age = int(i)

    except ValueError:
        print("That's not a digit! NUMBERS ONLY")
        continue

    if age <= 2:
        price = 0 

    elif age >= 3 and age <= 12:
        price = 10

    else: 
        price = 15

    family_age_group.append(price)
    final_price += price

    print(f"{age} you said... ... ticket for them costs: {price}!")
print(f"total price is: {final_price}")



# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.

# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.

teenagers = ["Ofir", "Nadav", "Nimrod", "Noa", "Eidan"]

oldEnough = []

for teen in teenagers:
    age = int(input(f"how old is {teen}? "))
# At the end, print the final list.
    print(f"{teen} is {age} years old.")

    if 16 <= age <=21:
        oldEnough.append(teen)

print(f"only {' ,'.join(oldEnough)} are allowed in")
        
    

################################################################################################

# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
finished_sandwiches = []
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
while sandwich_orders: 
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich}")

    #goes through the sandwich_orders and takes each first index (string) in the list except for pastrami which has been removed and adds it to the finished sandwhiches one by one

# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich





