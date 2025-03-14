# 🌟 Exercise 1 : Convert lists into dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

pairing = dict(zip(keys, values))
#converts paired data into dict.
print(pairing)


# 🌟 Exercise 2 : Cinemax #2
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

full_price = 0
for name, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    
    full_price += cost
    print(f"{name} has to pay ${cost}")

print(f"The total price for you all is: ${full_price}")


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

bonus_family = {}
party_amount = int(input(f"Enter the number of family members: "))

for _ in range(party_amount):
    name = input(f"Enter name of party member: ")
    age = int(input(f"How old is {name}? "))
    bonus_family[name] = age

final_price = 0

for name, age in bonus_family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    final_price += price
    print(f"The cost for {name} is ${price}.")

print(f"The total cost for your complete party is ${final_price}")


# 🌟 Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand = {
    "name": "Zara", 
    "creation_date" : 1975,
    "creator_name": "Amancio Ortega Gaona", 
    "type_of_clothes": ["men", "women, children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US": ["pink", "green"]
        }
    }
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
# 3. Change the number of stores to 2.
brand["number_stores"] = 2
# 4. Print a sentence that explains who Zaras clients are.
print(f"{name} has a variety of clients including men, women, and children")
# 5. Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
# 7. Delete the information about the date of creation.
del brand["creation_date"]
# 8. Print the last international competitor.
print(brand["international_competitors"][-1])
# 9. Print the major clothes colors in the US.
print(brand["major_color"]["US"])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))
# 11. Print the keys of the dictionary.
print(brand.keys())
# 12. Create another dictionary called more_on_zara with the following details:
more_on_zara ={
    "creation_date": 1975, 
    "number_stores": 10000
}
# creation_date: 1975 
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

#using update method
brand.update(more_on_zara)
# 14. Print the value of the key number_stores. What just happened ?
print(brand["number_stores"])


# Exercise 4 : Disney characters
# Instructions
# Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
disney_users_A = {user: index for index, user in enumerate(users)}
print(disney_users_A)
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
disney_users_B = {index: user for index, user in enumerate(users)}
print(disney_users_B)
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
disney_users_C = {user: index for index, user in enumerate(sorted(users))}
print(disney_users_C)
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
disney_users_with_i = {user: index for index, user in enumerate(users) if "i" in user.lower()}
print(disney_users_with_i)
# The characters, which names start with the letter “m” or “p”.
disney_users_mORp = {user: index for index, user in enumerate(users) if user[0].lower() in ["m", "p"]}
print(disney_users_mORp)