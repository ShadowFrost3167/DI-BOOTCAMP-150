import time
#wanted to for the song exercise

# 🌟 Exercise 1: Cats
# Instructions

# Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

#     Instantiate three Cat objects using the code provided above.

cat1 = Cat("Marie", 5)
cat2 = Cat("Toulouse", 6)
cat3 = Cat("Berlioz", 7)

    #Outside of the class, create a function that finds the oldest cat and returns the cat.

def oldest_cat(cat1, cat2, cat3):
    oldest_age = max(cat1.age, cat2.age, cat3.age)

    if cat1.age == oldest_age:
        return cat1
    elif cat2.age == oldest_age:
        return cat2
    else:
        return cat3


#     Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

tommiestTom = oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {tommiestTom.name}, and he is {tommiestTom.age} years old.")

# 🌟 Exercise 2 : Dogs
# Instructions

#     Create a class called Dog.
class Dog:

    #In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.

    def __init__(self, name, height):
        self.name = name
        self.height = height
    #Create a method called bark that prints the following string “<dog_name> goes woof!”.
    def bark(self):
        print(f"{self.name} goes woof!")
    #Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} will jump {jump_height}")
#     Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.


#     Print the details of his dog (ie. name and height) and call the methods bark and jump.
#     Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
#     Print the details of her dog (ie. name and height) and call the methods bark and jump.
#     Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

print (f"{davids_dog.name} is Davids dog measuring at {davids_dog.height} CM! {sarahs_dog.name} is Sarahs dog measuring in at {sarahs_dog.height} CM!")
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height >= sarahs_dog.height:
    print(f"{davids_dog.name}")
else:
    print(f"{sarahs_dog.name}")

# 🌟 Exercise 3 : Who’s the song producer?
# Instructions

#     Define a class called Song, it will show the lyrics of a song.
#     Its __init__() method should have two arguments: self and lyrics (a list).
#     Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

#     Create an object, for example:

#     stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


#     Then, call the sing_me_a_song method. The output should be:

#     There’s a lady who's sure
#     all that glitters is gold
#     and she’s buying a stairway to heaven


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            time.sleep(1)


bangDrum = Song([
    "I don't want to work",
    "I want to bang on the drum all day",
    "I don't want to play",
    "I just want to bang on the drum all day"
])

bangDrum.sing_me_a_song()



# Exercise 4 : Afternoon at the Zoo
# Instructions

#     Create a class called Zoo.
#     In this class create a method __init__ that takes one parameter: zoo_name.

class Zoo:
    def __init__(self, zoo_name):
        
#     It instantiates two attributes: animals (an empty list) and name (name of the zoo).
        self.name = zoo_name
        self.animals = []
#     Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo")
        else:
            print(f"{new_animal} is already at the zoo")
#     Create a method called get_animals that prints all the animals of the zoo.
    def get_animals(self):
        if not self.animals:
            print(f"we have no more animals left in the zoo")
        else:
            print("Animals in the zoo: ")
            for animal in self.animals:
                print(animal)
#     Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
#     Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
#     Example

#     { 
#         A: "Ape",
#         B: ["Baboon", "Bear"],
#         C: ['Cat', 'Cougar'],
#         E: ['Eel', 'Emu']
#     }

    def sort_animals(self):
        self.animals.sort()
        grouped_animals = {}
        
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        
        return grouped_animals
#     Create a method called get_groups that prints the animal/animals inside each group.

    def get_groups(self):
        grouped_animals = self.sort_animals()
        if not grouped_animals:
            print("No animals to group.")
        else:
            print("Animals grouped by their first letter:")
            for letter, animals in grouped_animals.items():
                print(f"{letter}: {', '.join(animals)}")
#     Create an object called ramat_gan_safari and call all the methods.

ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Lion") 

ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Zebra")
ramat_gan_safari.get_groups()

#     Tip: The zookeeper is the one who will use this class.
#     Example

#     Which animal should we add to the zoo --> Giraffe
#     x.add_animal(Giraffe)


