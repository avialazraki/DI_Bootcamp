
# Week 2 - Day 3 - Daily Challenge
# Find all pairs of numbers that sum to the target

import random

# Generate 20,000 random numbers
list_of_numbers = [
    random.randint(0, 10000)
    for _ in range(20000)
]

target_number = 3728

# Store numbers already encountered
seen_numbers = set()

# Store unique pairs
pairs = set()

# Find pairs that add up to the target
for number in list_of_numbers:

    complement = target_number - number

    # Check whether the matching number exists
    if complement in seen_numbers:

        # Sort the pair to avoid duplicates such as
        # (1000, 2728) and (2728, 1000)
        pair = tuple(sorted((number, complement)))
        pairs.add(pair)

    seen_numbers.add(number)

# Print the results
print("Target number:", target_number)
print("Total unique pairs found:", len(pairs))

print("\nPairs that sum to the target:")

for number1, number2 in sorted(pairs):
    print(f"{number1} + {number2} = {target_number}")
