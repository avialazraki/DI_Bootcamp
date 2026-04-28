# Challenge 1: Multiples of a Number
#
#
# Key Python Topics:
# input() function
# Loops (for or while)
# Lists and appending items
# Basic arithmetic (multiplication)
#
#
# Instructions:
# 1. Ask the user for two inputs:
#
# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

# 1. Ask the user for two integer inputs
# We use int() to convert the string input into an integer for math
num = int(input("Enter the base number: "))
length = int(input("Enter the required length: "))

# 2. & 3. Generate a list of multiples that stops at the specified length
# A list comprehension provides a concise way to create this list
multiples = [num * i for i in range(1, length + 1)]

# Output the final list
print(f"List of {length} multiples of {num}:")
print(multiples)

# Challenge 2: Remove Consecutive Duplicate Letters
#
#
# Key Python Topics:
# input() function
# Strings and string manipulation
# Loops (for or while)
# Conditional statements (if)
#
#
# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
#
# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.
#
user_input = input("Enter a string: ")
modified_string = ""

for char in user_input:
    # If modified_string is empty or the current char is different from the last added char
    if not modified_string or char != modified_string[-1]:
        modified_string += char

print(modified_string)