
# Week 2 - Day 2 - Daily Challenge
# Matrix Decoder

import re

# Step 1: Define the original matrix
MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

# Convert the string into a 2D list
matrix = [list(row) for row in MATRIX_STR.strip("\n").splitlines()]

# Ensure all rows have the same number of columns
columns = max(len(row) for row in matrix)

for row in matrix:
    while len(row) < columns:
        row.append(" ")

# Step 2: Read the matrix column by column
column_text = ""

for col in range(columns):
    for row in range(len(matrix)):
        column_text += matrix[row][col]

# Step 3: Replace groups of symbols between letters
decoded_message = re.sub(
    r"[^A-Za-z]+",
    " ",
    column_text
).strip()

# Step 4: Display the result
print("Decoded message:", decoded_message)
