
# ============================================================
# WEEK 2 - DAY 4 - HANGMAN GAME
# ============================================================

# Instructions:
# 1. The computer chooses a random word.
# 2. Display stars (*) for each hidden letter.
# 3. The player guesses one letter at a time.
# 4. Correct guesses reveal all matching letters.
# 5. Wrong guesses add a body part to the gallows.
# 6. The player loses after six incorrect guesses.
# 7. The player wins by guessing all letters.
# 8. The same letter cannot be guessed twice.

import random

# Starter code
wordslist = [
    'correction', 'childish', 'beach', 'python',
    'assertive', 'interference', 'complete',
    'share', 'credit card', 'rush', 'south'
]

word = random.choice(wordslist)

# Gallows drawings for 0 to 6 incorrect guesses
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")
print("Guess the hidden word or phrase.")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_wrong_guesses:

    # Show the word with hidden letters
    display_word = ""

    for letter in word:
        if letter == " ":
            display_word += " "
        elif letter in guessed_letters:
            display_word += letter
        else:
            display_word += "*"

    # Display the gallows and current progress
    print(hangman_stages[wrong_guesses])
    print("Word:", display_word)
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Incorrect guesses left:", max_wrong_guesses - wrong_guesses)

    # Check if all letters have been guessed
    if "*" not in display_word:
        print("\nCongratulations! You won!")
        print("The word was:", word)
        break

    # Ask the player for a letter
    guess = input("\nGuess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Prevent repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    # Player has used all six incorrect guesses
    print(hangman_stages[wrong_guesses])
    print("\nGame Over! You lost.")
    print("The word was:", word)
