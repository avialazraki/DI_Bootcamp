#Exercise 4 : How many characters in a sentence ?
#Instructions
#Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

#Exercise 5: Longest word without a specific character
#Instructions
#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.

def longest_sentence_without_a():
    """
    Asks the user to input sentences without the letter 'a' (case-insensitive)
    and tracks the longest one.
    """
    longest_sentence = ""

    print("Welcome to the 'No A' Longest Sentence Challenge!")
    print("Type 'quit' to end the game.\n")

    while True:
        # Get input from the user
        sentence = input("Enter a sentence without the letter 'A': ")

        # Allow user to quit
        if sentence.lower() == 'quit':
            break

        # Check if 'a' (or 'A') is in the sentence
        if 'a' in sentence.lower():
            print("Invalid input! Your sentence contained the letter 'A'. Try again.")
            continue

        # Check if it's the new longest sentence
        if len(sentence) > len(longest_sentence):
            longest_sentence = sentence
            print(f"🎉 Congratulations! New longest sentence set ({len(longest_sentence)} characters).")
        else:
            print(f"Not quite! Current record is {len(longest_sentence)} characters.")

    print(f"\nGame Over! Your longest sentence was: '{longest_sentence}'")


# Run the function
longest_sentence_without_a()