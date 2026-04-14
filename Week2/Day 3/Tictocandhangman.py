#Mini-Project - Tic Tac Toe

board = [" " for _ in range(9)]

def display_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6: print("-" * 9)

def check_win(p):
    win_cond = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == p for a, b, c in win_cond)

def player_input():
    current = "X"
    for turn in range(9):
        display_board()
        move = int(input(f"Player {current}, choose (1-9): ")) - 1
        if board[move] == " ":
            board[move] = current
            if check_win(current):
                display_board()
                print(f"Player {current} wins!")
                return
            current = "O" if current == "X" else "X"
        else:
            print("Taken!")
    print("Tie!")

player_input()

#Mini-Project - HANGMAN
import random


def play_hangman():
    words = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = []
    max_wrong = 6

    # Body parts to add for each wrong guess
    stages = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",  # Initial
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",  # Head
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",  # Body
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",  # Left Arm
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",  # Right Arm
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",  # Left Leg
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="  # Right Leg
    ]

    print("Welcome to Hangman!")

    while len(wrong_guesses) < max_wrong:
        # Display current word state
        display_word = "".join([letter if letter in guessed_letters or letter == " " else "*"
    for letter in word])
        print(stages[len(wrong_guesses)])
        print(f"\nWord: {display_word}")
        print(f"Guessed: {', '.join(sorted(guessed_letters))}")

        if "*" not in display_word:
            print(f"\nCongratulations! You guessed the word: {word}")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_guesses.append(guess)
            print(f"Sorry, '{guess}' is not there.")

    print(stages[6])
    print(f"\nGame Over! The word was: {word}")


if __name__ == "__main__":
    play_hangman()