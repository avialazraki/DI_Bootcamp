
from pathlib import Path


class AnagramChecker:
    def __init__(self):
        # Load the English word list when the class is created.
        file_path = Path(__file__).resolve().parent / "sowpods.txt"

        with open(file_path, "r", encoding="utf-8") as file:
            self.words = {
                word.strip().upper()
                for word in file
                if word.strip()
            }

    def is_valid_word(self, word):
        # Check if the word exists in the English dictionary.
        return word.strip().upper() in self.words

    def is_anagram(self, word1, word2):
        # Compare letters, excluding identical words.
        word1 = word1.strip().upper()
        word2 = word2.strip().upper()

        return word1 != word2 and sorted(word1) == sorted(word2)

    def get_anagrams(self, word):
        # Find every dictionary word with the same letters.
        word = word.strip().upper()

        anagrams = []

        for dictionary_word in self.words:
            if self.is_anagram(word, dictionary_word):
                anagrams.append(dictionary_word.lower())

        return sorted(anagrams)
