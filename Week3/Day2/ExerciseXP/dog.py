
# WEEK 3 - DAY 2 - EXERCISE 2: DOGS
#
# Create a Dog class with name, age, and weight attributes.
# Implement bark(), run_speed(), and fight(other_dog).
# Running speed = weight / age * 10.
# Fighting strength = running speed * weight.


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight

        if my_strength > other_strength:
            return f"{self.name} wins the fight!"
        elif other_strength > my_strength:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"
