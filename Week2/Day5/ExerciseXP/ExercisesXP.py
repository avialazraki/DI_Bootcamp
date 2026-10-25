
# ============================================
# Week 2 - Day 5 - Exercises XP
# ============================================


# ============================================
# Exercise 1: Cats
# ============================================

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Tom", 3)
cat2 = Cat("Luna", 7)
cat3 = Cat("Simba", 5)


def find_oldest_cat(cat1, cat2, cat3):
    oldest_cat = cat1

    if cat2.age > oldest_cat.age:
        oldest_cat = cat2

    if cat3.age > oldest_cat.age:
        oldest_cat = cat3

    return oldest_cat


print("Exercise 1: Cats")

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(
    f"The oldest cat is {oldest_cat.name}, "
    f"and is {oldest_cat.age} years old."
)


# ============================================
# Exercise 2: Dogs
# ============================================

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


print("\nExercise 2: Dogs")

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 40)

print(f"David's dog: {davids_dog.name}, height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog: {sarahs_dog.name}, height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the bigger dog.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is the bigger dog.")
else:
    print("Both dogs are the same height.")


# ============================================
# Exercise 3: Who's the Song Producer?
# ============================================

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


print("\nExercise 3: Song")

# Original example lyrics are replaced with
# custom lines to demonstrate the same method.
my_song = Song([
    "The morning sun is shining bright",
    "The birds are singing in the light",
    "A brand new day is here again"
])

my_song.sing_me_a_song()


# ============================================
# Exercise 4: Afternoon at the Zoo
# ============================================

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.animal_groups = {}

    # Bonus: Accept multiple animals using *args
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(f"{self.zoo_name} animals:")
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        self.animals.sort()

        self.animal_groups = {}

        for animal in self.animals:
            first_letter = animal[0].upper()

            if first_letter not in self.animal_groups:
                self.animal_groups[first_letter] = []

            self.animal_groups[first_letter].append(animal)

        return self.animal_groups

    def get_groups(self):
        for letter, animals in self.animal_groups.items():
            print(f"{letter}: {animals}")


print("\nExercise 4: Afternoon at the Zoo")

brooklyn_safari = Zoo("Brooklyn Safari")

# Add multiple animals (bonus)
brooklyn_safari.add_animal(
    "Giraffe",
    "Bear",
    "Baboon",
    "Cat",
    "Cougar",
    "Lion",
    "Zebra"
)

# Test duplicate prevention
brooklyn_safari.add_animal("Lion")

print("\nAnimals before selling:")
brooklyn_safari.get_animals()

print("\nSelling Bear:")
brooklyn_safari.sell_animal("Bear")

print("\nAnimals after selling:")
brooklyn_safari.get_animals()

print("\nSorted animal groups:")
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
