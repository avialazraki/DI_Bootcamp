
# ============================================
# Week 3 - Day 5 - Daily Challenge
# Text Analysis and Text Modification
# ============================================

import string
import re
from pathlib import Path


# ============================================
# Part I: Text Analysis
# ============================================

class Text:

    # Step 1: Initialize the Text class
    def __init__(self, text):
        self.text = text

    # Step 2: Count occurrences of a word
    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)

        if count == 0:
            return None

        return count

    # Step 3: Find the most common word
    def most_common_word(self):
        words = self.text.split()

        if not words:
            return None

        frequencies = {}

        for word in words:
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1

        most_common = max(frequencies, key=frequencies.get)

        return most_common

    # Step 4: Get unique words
    def unique_words(self):
        words = self.text.split()

        unique = set(words)

        return sorted(list(unique))

    # ========================================
    # Part II: Text from a File
    # ========================================

    # Step 5: Create a Text object from a file
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return cls(content)


# ============================================
# Bonus: Text Modification
# ============================================

class TextModification(Text):

    # Step 7: Remove punctuation
    def remove_punctuation(self):
        translator = str.maketrans(
            "", "", string.punctuation
        )

        return self.text.translate(translator)

    # Step 8: Remove English stop words
    def remove_stop_words(self):

        # Common English stop words
        stop_words = {
            "a", "an", "the", "and", "or", "but",
            "is", "are", "was", "were", "be",
            "been", "being", "am", "to", "of",
            "in", "on", "at", "for", "with",
            "by", "from", "as", "that", "this",
            "these", "those", "it", "its",
            "i", "you", "he", "she", "we", "they",
            "me", "him", "her", "us", "them",
            "my", "your", "his", "our", "their",
            "do", "does", "did", "have", "has",
            "had", "not", "so", "if", "then",
            "than", "there", "here", "who",
            "what", "when", "where", "why",
            "how", "can", "could", "would",
            "should", "will", "just"
        }

        words = self.text.split()

        filtered_words = []

        for word in words:
            clean_word = word.strip(
                string.punctuation
            ).lower()

            if clean_word not in stop_words:
                filtered_words.append(word)

        return " ".join(filtered_words)

    # Step 9: Remove special characters
    def remove_special_characters(self):
        cleaned_text = re.sub(
            r"[^a-zA-Z0-9\s]", "", self.text
        )

        return cleaned_text


# ============================================
# Testing Part I: Text Analysis
# ============================================

print("WEEK 3 - DAY 5 - DAILY CHALLENGE")

sample_text = (
    "Python is fun Python is powerful "
    "Python is easy to learn"
)

text_object = Text(sample_text)

print("\nPART I: TEXT ANALYSIS")

print("Original text:")
print(text_object.text)

print("\nFrequency of 'Python':")
print(text_object.word_frequency("Python"))

print("\nFrequency of 'Java':")
print(text_object.word_frequency("Java"))

print("\nMost common word:")
print(text_object.most_common_word())

print("\nUnique words:")
print(text_object.unique_words())


# ============================================
# Testing Part II: File Handling
# ============================================

print("\nPART II: TEXT FROM FILE")

# Create a sample text file beside this script
sample_file = Path(__file__).resolve().parent / "sample_text.txt"

with open(sample_file, "w", encoding="utf-8") as file:
    file.write(
        "Python is great. Python is useful. "
        "Learning Python is fun!"
    )

file_text = Text.from_file(sample_file)

print("Text loaded from file:")
print(file_text.text)

print("\nMost common word in file:")
print(file_text.most_common_word())


# ============================================
# Testing Bonus: Text Modification
# ============================================

print("\nBONUS: TEXT MODIFICATION")

modification = TextModification(
    "Hello, world! Python is amazing. "
    "The world is full of possibilities! #2026"
)

print("\nOriginal text:")
print(modification.text)

print("\nRemove punctuation:")
print(modification.remove_punctuation())

print("\nRemove stop words:")
print(modification.remove_stop_words())

print("\nRemove special characters:")
print(modification.remove_special_characters())
