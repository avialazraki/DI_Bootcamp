
from anagram_checker import AnagramChecker


def main():
    checker = AnagramChecker()

    print("=" * 45)
    print("       WELCOME TO ANAGRAM CHECKER")
    print("=" * 45)

    while True:
        print("\nMENU")
        print("1. Enter a word")
        print("2. Exit")

        choice = input("\nChoose an option (1 or 2): ").strip()

        if choice == "2":
            print("\nThank you for using Anagram Checker!")
            break

        elif choice == "1":
            user_input = input("\nEnter a word: ").strip()

            # Only one word is allowed.
            if len(user_input.split()) != 1:
                print("Error: Please enter exactly one word.")
                continue

            # Only letters are allowed.
            if not user_input.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue

            word = user_input.upper()

            print("\n" + "=" * 45)
            print(f'YOUR WORD: "{word}"')

            if checker.is_valid_word(word):
                print("This is a valid English word.")

                anagrams = checker.get_anagrams(word)

                if anagrams:
                    print("Anagrams for your word: " + ", ".join(anagrams))
                else:
                    print("No anagrams found.")
            else:
                print("This is not a valid English word.")

            print("=" * 45)

        else:
            print("Invalid menu option. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
