
import random

# ============================================================
# WEEK 2 - DAY 2 - EXERCISES XP
# ============================================================

# Exercise 1: What Are You Learning?
# Define display_message() without parameters.
# Print a message about what you are learning.
# Call the function.

def display_message():
    print("I am learning about functions in Python.")

display_message()


# Exercise 2: What's Your Favorite Book?
# Define favorite_book() with a title parameter.
# Print a message containing the book title.
# Call the function with a book title.

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")


# Exercise 3: Some Geography
# Define describe_city() with city and country parameters.
# Set the default country to "Unknown".
# Print the city and country.
# Call with and without a country argument.

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")


# Exercise 4: Random
# Accept a number between 1 and 100.
# Generate a random integer between 1 and 100.
# Print success if the numbers match.
# Otherwise print both numbers.

def compare_random_numbers(number):
    random_number = random.randint(1, 100)

    if number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {number}, Random number: {random_number}")

compare_random_numbers(50)


# Exercise 5: Personalized Shirts
# Define make_shirt() with size and text parameters.
# Set default size="large" and text="I love Python".
# Print the shirt size and message.
# Call with default and custom values.
# Bonus: Use keyword arguments.

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="Custom message")
make_shirt(text="Hello!", size="small")


# Exercise 6: Magicians
# Create a list of magician names.
# Define show_magicians() to print each name.
# Define make_great() to add "the Great" to each name.
# Modify the list and display the results.

magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for index in range(len(names)):
        names[index] = names[index] + " the Great"

make_great(magician_names)
show_magicians(magician_names)


# Exercise 7: Temperature Advice
# Generate a random temperature between -10 and 40 Celsius.
# Display the temperature and appropriate advice.
# Bonus: Generate floating-point temperatures.
# Bonus: Ask for a month and generate seasonal temperatures.

def get_random_temp(month=None):
    if month is None:
        return random.uniform(-10, 40)

    if month in [12, 1, 2]:
        return random.uniform(-10, 16)
    elif month in [3, 4, 5]:
        return random.uniform(5, 23)
    elif month in [6, 7, 8]:
        return random.uniform(20, 40)
    else:
        return random.uniform(5, 25)


def main():
    while True:
        try:
            month = int(input("Enter a month (1-12): "))
            if 1 <= month <= 12:
                break
            print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    temperature = get_random_temp(month)
    print(f"The temperature right now is {temperature:.1f} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temperature < 24:
        print("Nice weather.")
    elif temperature < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")


main()
