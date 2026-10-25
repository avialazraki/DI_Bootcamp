
# ============================================
# Week 2 - Day 5 - Daily Challenge
# Old MacDonald's Farm
# ============================================

class Farm:

    # Step 1 & 2: Initialize the farm
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    # Step 3 & Bonus Step 8: Add animals
    def add_animal(self, animal_type=None, count=1, **kwargs):

        # Add a single animal type
        if animal_type is not None:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

        # Bonus: Add multiple animal types using **kwargs
        for animal, quantity in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += quantity
            else:
                self.animals[animal] = quantity

    # Step 4: Display farm information
    def get_info(self):
        info = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            info += f"{animal:<8} : {count}\n"

        info += "\n    E-I-E-I-0!"

        return info

    # Bonus Step 6: Get sorted animal types
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Bonus Step 7: Short farm description
    def get_short_info(self):
        animal_types = self.get_animal_types()

        animal_names = []

        for animal in animal_types:
            if self.animals[animal] > 1:
                animal_names.append(animal + "s")
            else:
                animal_names.append(animal)

        if len(animal_names) == 0:
            animals_text = "no animals"
        elif len(animal_names) == 1:
            animals_text = animal_names[0]
        else:
            animals_text = (
                ", ".join(animal_names[:-1])
                + " and "
                + animal_names[-1]
            )

        return f"{self.name}'s farm has {animals_text}."


# ============================================
# Test the original assignment
# ============================================

macdonald = Farm("McDonald")

macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)

print("Original Challenge:")
print(macdonald.get_info())

# ============================================
# Test the bonus methods
# ============================================

print("\nBonus - Sorted Animal Types:")
print(macdonald.get_animal_types())

print("\nBonus - Short Farm Information:")
print(macdonald.get_short_info())

# ============================================
# Test Bonus: **kwargs
# ============================================

print("\nBonus - Adding Multiple Animals:")

macdonald.add_animal(
    horse=2,
    chicken=4,
    duck=3
)

print(macdonald.get_info())

