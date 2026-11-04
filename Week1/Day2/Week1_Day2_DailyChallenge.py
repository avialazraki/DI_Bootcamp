"""Week 1 Day 2 - Daily Challenge: Python basics, conditionals, loops."""
import random

user_string = input("Enter a string of exactly 10 characters: ")

if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
else:
    print("Perfect string")
    print("First character:", user_string[0])
    print("Last character:", user_string[-1])

    growing_string = ""
    for character in user_string:
        growing_string += character
        print(growing_string)

    characters = list(user_string)
    random.shuffle(characters)
    print("Shuffled string:", "".join(characters))
