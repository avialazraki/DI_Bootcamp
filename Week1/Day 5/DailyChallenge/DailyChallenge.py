
# Week 1 - Day 5 - Daily Challenge
# Challenge 1: Letter Index Dictionary

word = input("Enter a word: ")

letter_indices = {}

for index, letter in enumerate(word):
    if letter in letter_indices:
        letter_indices[letter].append(index)
    else:
        letter_indices[letter] = [index]

print(letter_indices)


# Challenge 2: Affordable Items



items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"





# Remove dollar signs and commas from the wallet
wallet = int(wallet.replace("$", "").replace(",", ""))

# Create an empty shopping basket
basket = []

# Process items in dictionary order (priority order)
for item, price in items_purchase.items():

    # Remove dollar signs and commas from the price
    price = int(price.replace("$", "").replace(",", ""))

    # Buy the item if enough money remains
    if price <= wallet:
        basket.append(item)
        wallet -= price

# Display the basket alphabetically
if basket:
    print(sorted(basket))
else:
    print("Nothing")


items_purchase = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2"
}

wallet = "$100"
