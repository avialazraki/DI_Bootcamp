
# ============================================================
# WEEK 3 - DAY 2 - EXERCISES XP
# Topics: Inheritance, Classes, Polymorphism, super(), Methods
# ============================================================

import random
from dog import Dog


# ============================================================
# EXERCISE 1: PETS
# ============================================================
# Create a Siamese class that inherits from Cat.
# Create Bengal, Chartreux, and Siamese cat instances.
# Store them in all_cats.
# Create sara_pets using the Pets class.
# Call sara_pets.walk() to display all cats walking.


class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Siamese(Cat):
    pass


all_cats = [
    Bengal("Leo", 3),
    Chartreux("Luna", 2),
    Siamese("Milo", 4)
]

sara_pets = Pets(all_cats)

print("\n--- Exercise 1: Pets ---")
sara_pets.walk()


# ============================================================
# EXERCISE 2: DOGS
# ============================================================
# The Dog class is defined in dog.py.
# Create three Dog instances.
# Test bark(), run_speed(), and fight().


print("\n--- Exercise 2: Dogs ---")

dog1 = Dog("Max", 3, 20)
dog2 = Dog("Buddy", 5, 25)
dog3 = Dog("Rocky", 2, 15)

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(f"{dog1.name}'s running speed: {dog1.run_speed():.2f}")
print(f"{dog2.name}'s running speed: {dog2.run_speed():.2f}")
print(f"{dog3.name}'s running speed: {dog3.run_speed():.2f}")

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))


# ============================================================
# EXERCISE 3: DOGS DOMESTICATED
# ============================================================
# Import Dog from the previous exercise.
# Create PetDog as a subclass of Dog.
# Add a trained attribute, default False.
# train() should print bark() and set trained to True.
# play(*args) should print all dogs playing together.
# do_a_trick() should print a random trick if trained.
# Test all methods.


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name]

        for dog in args:
            if isinstance(dog, Dog):
                dog_names.append(dog.name)
            else:
                dog_names.append(str(dog))

        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} needs training first.")


print("\n--- Exercise 3: Dogs Domesticated ---")

pet1 = PetDog("Fido", 2, 10)
pet2 = PetDog("Charlie", 3, 18)
pet3 = PetDog("Bella", 4, 15)

pet1.do_a_trick()

pet1.train()
pet2.train()
pet3.train()

pet1.play(pet2, pet3)

pet1.do_a_trick()
pet2.do_a_trick()
pet3.do_a_trick()


# ============================================================
# EXERCISE 4: FAMILY AND PERSON CLASSES
# ============================================================
# Create Person with first_name, age, and last_name.
# Initialize last_name as an empty string.
# is_18() returns True if the person is 18 or older.
#
# Create Family with last_name and an empty members list.
# born(first_name, age) creates and adds a Person.
# check_majority(first_name) checks if a member is an adult.
# family_presentation() displays the family and its members.
# Create a family and test all methods.


class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(
                        "You are over 18, your parents Jane and John "
                        "accept that you will go out with your friends"
                    )
                else:
                    print(
                        "Sorry, you are not allowed to go out "
                        "with your friends."
                    )
                return

        print(f"{first_name} was not found in the family.")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")

        for person in self.members:
            print(f"Name: {person.first_name}, Age: {person.age}")


print("\n--- Exercise 4: Family and Person ---")

my_family = Family("Smith")

my_family.born("Jane", 42)
my_family.born("John", 45)
my_family.born("Alice", 20)
my_family.born("Tom", 15)

my_family.family_presentation()

print("\nChecking majority:")
my_family.check_majority("Alice")
my_family.check_majority("Tom")
