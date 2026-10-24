
# ============================================================
# WEEK 3 - DAY 5 - EXERCISES XP
# Topics: File Handling, Random, Lists, Strings, JSON
# ============================================================

import random
import json
from pathlib import Path

# Get the directory containing this Python file.
# This allows the program to find words.txt even when
# PyCharm uses a different working directory.
BASE_DIR = Path(__file__).resolve().parent
WORDS_FILE = BASE_DIR / "words.txt"


# ============================================================
# EXERCISE 1: RANDOM SENTENCE GENERATOR
# ============================================================
# Read words from a text file.
# Generate a random sentence of a requested length.
# Validate that the length is an integer between 2 and 20.


def get_words_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    words = content.split()
    return words


def get_random_sentence(length):
    words = get_words_from_file(WORDS_FILE)

    if not words:
        raise ValueError("The word list is empty.")

    selected_words = []

    for i in range(length):
        selected_words.append(random.choice(words))

    sentence = " ".join(selected_words).lower()
    return sentence


def main():
    print("\n--- Exercise 1: Random Sentence Generator ---")
    print("This program generates a random sentence from a word list.")
    print("Choose a sentence length between 2 and 20 words.")

    user_input = input("Enter the sentence length: ")

    try:
        length = int(user_input)

        if length < 2 or length > 20:
            print("Error: The length must be between 2 and 20.")
            return

        sentence = get_random_sentence(length)
        print(f"Generated sentence: {sentence}")

    except ValueError as error:
        print(f"Error: {error}")

    except FileNotFoundError:
        print("Error: words.txt was not found.")
        print("Please place words.txt in the same folder as this script.")

    except OSError as error:
        print(f"Error reading the word list: {error}")


# ============================================================
# EXERCISE 2: WORKING WITH JSON
# ============================================================
# Parse the sample JSON string.
# Access the employee's salary.
# Add a birth_date to the employee dictionary.
# Save the modified data to employee.json.


def working_with_json():
    print("\n--- Exercise 2: Working with JSON ---")

    sampleJson = """
    {
        "company": {
            "employee": {
                "name": "emma",
                "payable": {
                    "salary": 7000,
                    "bonus": 800
                }
            }
        }
    }
    """

    # Step 1: Convert the JSON string into a dictionary.
    data = json.loads(sampleJson)

    # Step 2: Access the nested salary value.
    salary = data["company"]["employee"]["payable"]["salary"]

    print(f"Employee salary: {salary}")

    # Step 3: Add a birth_date to the employee dictionary.
    data["company"]["employee"]["birth_date"] = "1995-06-15"

    print(
        "Employee birth date:",
        data["company"]["employee"]["birth_date"]
    )

    # Step 4: Save the updated dictionary as a JSON file.
    output_file = BASE_DIR / "employee.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Modified JSON saved to: {output_file}")

    # Display the updated JSON.
    print("\nUpdated JSON:")
    print(json.dumps(data, indent=4))


# ============================================================
# RUN BOTH EXERCISES
# ============================================================

if __name__ == "__main__":
    main()
    working_with_json()
