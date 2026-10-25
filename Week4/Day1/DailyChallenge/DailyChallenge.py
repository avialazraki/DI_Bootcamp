
# ============================================
# Week 4 - Day 1 - Daily Challenges
# OOP Quiz and Deck of Cards
# ============================================

# ============================================
# PART 1: OOP QUIZ
# ============================================

# 1. What is a class?
# A class is a blueprint for creating objects.
# It defines attributes and methods.

# 2. What is an instance?
# An instance is an object created from a class.
# Each instance can have its own attribute values.

# 3. What is encapsulation?
# Encapsulation combines data and methods in a
# class and controls access to internal details.

# 4. What is abstraction?
# Abstraction hides unnecessary implementation
# details and exposes essential functionality.

# 5. What is inheritance?
# Inheritance allows a child class to reuse
# and extend the behavior of a parent class.

# 6. What is multiple inheritance?
# Multiple inheritance allows a class to
# inherit from more than one parent class.

# 7. What is polymorphism?
# Polymorphism allows different objects to
# respond to the same method or operation.

# 8. What is Method Resolution Order (MRO)?
# MRO is the order Python follows when searching
# for methods and attributes in inherited classes.


# ============================================
# PART 2: DECK OF CARDS
# ============================================

import random


# Step 1: Create the Card class
class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return self.__str__()


# Step 2: Create the Deck class
# Deck does NOT inherit from Card
class Deck:

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    values = [
        "A", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "J", "Q", "K"
    ]

    def __init__(self):
        # Create all 52 unique cards
        self.cards = [
            Card(suit, value)
            for suit in self.suits
            for value in self.values
        ]

    # Shuffle the deck
    def shuffle(self):
        # Ensure the deck contains all 52 unique cards
        if len(self.cards) != 52:
            raise ValueError(
                "Cannot shuffle: the deck must contain 52 cards."
            )

        unique_cards = {
            (card.suit, card.value)
            for card in self.cards
        }

        if len(unique_cards) != 52:
            raise ValueError(
                "Cannot shuffle: the deck contains duplicate cards."
            )

        random.shuffle(self.cards)

    # Deal one card and remove it from the deck
    def deal(self):
        if not self.cards:
            return None

        return self.cards.pop()

    # Show how many cards remain
    def cards_remaining(self):
        return len(self.cards)


# ============================================
# TEST THE DECK OF CARDS
# ============================================

print("WEEK 4 - DAY 1 - DAILY CHALLENGE")

# Create a new deck
deck = Deck()

print("\nInitial number of cards:")
print(deck.cards_remaining())

# Shuffle all 52 cards
deck.shuffle()

print("\nDeck shuffled successfully!")

# Deal three cards
print("\nDealing three cards:")

for i in range(3):
    card = deck.deal()
    print(f"Card {i + 1}: {card}")

print("\nCards remaining:")
print(deck.cards_remaining())

# Verify that dealt cards are removed
print("\nTesting shuffle with fewer than 52 cards:")

try:
    deck.shuffle()
except ValueError as error:
    print("Error:", error)

# Create a new full deck
new_deck = Deck()

print("\nNew deck created:")
print(new_deck.cards_remaining())

# Deal every card
for i in range(52):
    new_deck.deal()

print("\nCards remaining after dealing all 52:")
print(new_deck.cards_remaining())

# Test dealing from an empty deck
print("\nDealing from an empty deck:")
print(new_deck.deal())
