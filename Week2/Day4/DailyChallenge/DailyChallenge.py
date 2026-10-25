
# Week 2 - Day 4 - Daily Challenges

# =====================================
# Challenge 1: Sorting
# =====================================

# Get comma-separated words from the user
words_input = input("Enter words separated by commas: ")

# Split the input into a list
words_list = words_input.split(",")

# Remove extra spaces around each word
words_list = [word.strip() for word in words_list]

# Sort the words alphabetically
words_list.sort()

# Join the sorted words with commas
sorted_words = ",".join(words_list)

# Display the result
print("Sorted words:", sorted_words)


# =====================================
# Challenge 2: Longest Word
# =====================================

def longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Handle an empty sentence
    if not words:
        return ""

    # Initialize with the first word
    longest = words[0]

    # Find the longest word
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


# Test the function with the assignment examples
print("\nChallenge 2: Longest Word")

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
