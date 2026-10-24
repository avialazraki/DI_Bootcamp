
# ============================================================
# WEEK 3 - DAY 4 - EXERCISES XP
# Topics: Dunder Methods, Modules, string, datetime, Faker
# ============================================================

import random
import string
import datetime
from faker import Faker

# ============================================================
# EXERCISE 1: CURRENCIES
# ============================================================
# Implement __str__, __repr__, __int__, __add__, and __iadd__.
# Allow adding integers and currencies of the same type.
# Raise TypeError for different currency types.


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        suffix = "" if self.amount == 1 else "s"
        return f"{self.amount} {self.currency}{suffix}"

    def __repr__(self):
        return str(self)

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type "
                    f"<{self.currency}> and <{other.currency}>"
                )
            return self.amount + other.amount

        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type "
                    f"<{self.currency}> and <{other.currency}>"
                )
            self.amount += other.amount
        else:
            return NotImplemented

        return self


print("\n--- Exercise 1: Currencies ---")

c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)

print(c1)
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)

c1 += 5
print(c1)

c1 += c2
print(c1)

# Test the expected TypeError without stopping other exercises.
try:
    print(c1 + c3)
except TypeError as error:
    print(f"TypeError: {error}")


# ============================================================
# EXERCISE 2: IMPORT
# ============================================================
# Create func.py with a function that adds two numbers.
# Import that function into exercise_one.py and call it.
# Both files are provided separately.
#
# We can also import the function here to test it.


print("\n--- Exercise 2: Import ---")

from func import add_numbers

add_numbers(10, 20)


# ============================================================
# EXERCISE 3: STRING MODULE
# ============================================================
# Generate a random string of 5 characters.
# Use uppercase and lowercase letters only.


print("\n--- Exercise 3: String Module ---")

letters = string.ascii_letters
random_string = ""

for i in range(5):
    random_string += random.choice(letters)

print(f"Random string: {random_string}")


# ============================================================
# EXERCISE 4: CURRENT DATE
# ============================================================
# Create a function that displays today's date.


def display_current_date():
    today = datetime.date.today()
    print(f"Current date: {today}")


print("\n--- Exercise 4: Current Date ---")
display_current_date()


# ============================================================
# EXERCISE 5: TIME LEFT UNTIL JANUARY 1ST
# ============================================================
# Calculate the time remaining until January 1st
# of the next year.


def time_until_new_year():
    now = datetime.datetime.now()

    next_new_year = datetime.datetime(now.year + 1, 1, 1)

    time_left = next_new_year - now

    print(f"Time left until January 1st: {time_left}")


print("\n--- Exercise 5: Time Until January 1st ---")
time_until_new_year()


# ============================================================
# EXERCISE 6: BIRTHDAY AND MINUTES
# ============================================================
# Accept a birthdate in YYYY-MM-DD format.
# Calculate the number of minutes lived.


def minutes_lived(birthdate):
    birth_datetime = datetime.datetime.strptime(
        birthdate, "%Y-%m-%d"
    )

    now = datetime.datetime.now()
    difference = now - birth_datetime

    if difference.total_seconds() < 0:
        print("Birthdate cannot be in the future.")
        return

    minutes = int(difference.total_seconds() / 60)

    print(f"You have lived approximately {minutes:,} minutes.")


print("\n--- Exercise 6: Birthday and Minutes ---")

minutes_lived("2000-01-01")


# ============================================================
# EXERCISE 7: FAKER MODULE
# ============================================================
# Generate fake user data.
# Store dictionaries with name, address, and language_code
# in a list.


fake = Faker()
users = []


def add_users(number_of_users):
    for i in range(number_of_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }

        users.append(user)


print("\n--- Exercise 7: Faker Module ---")

add_users(5)

for index, user in enumerate(users, start=1):
    print(f"\nUser {index}")
    print(f"Name: {user['name']}")
    print(f"Address: {user['address']}")
    print(f"Language Code: {user['language_code']}")
