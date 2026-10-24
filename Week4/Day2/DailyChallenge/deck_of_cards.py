
# Week 4 Day 2 - Daily Challenge
# Exercise 2: Deck of Cards

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return str(self)


class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = [
            "A", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K"
        ]

        self.cards = [
            Card(suit, value)
            for suit in self.suits
            for value in self.values
        ]

    def shuffle(self):
        # Shuffle only if the deck contains all 52 unique cards.
        if len(self.cards) != 52:
            print("Cannot shuffle: the deck does not contain 52 cards.")
            return

        unique_cards = {
            (card.suit, card.value)
            for card in self.cards
        }

        if len(unique_cards) != 52:
            print("Cannot shuffle: the deck contains duplicate cards.")
            return

        random.shuffle(self.cards)

    def deal(self):
        # Remove and return one card from the deck.
        if not self.cards:
            return None

        return self.cards.pop()


def main():
    print("=" * 40)
    print("       DECK OF CARDS")
    print("=" * 40)

    deck = Deck()

    print(f"\nNew deck created: {len(deck.cards)} cards")

    deck.shuffle()
    print("Deck shuffled successfully!")

    print("\nDealing 5 cards:")

    for i in range(5):
        card = deck.deal()
        print(f"Card {i + 1}: {card}")

    print(f"\nRemaining cards: {len(deck.cards)}")

    print("\nTrying to shuffle the incomplete deck:")
    deck.shuffle()

    print("\nDealing all remaining cards:")

    while deck.cards:
        deck.deal()

    print(f"Remaining cards: {len(deck.cards)}")
    print(f"Deal from empty deck: {deck.deal()}")


if __name__ == "__main__":
    main()
