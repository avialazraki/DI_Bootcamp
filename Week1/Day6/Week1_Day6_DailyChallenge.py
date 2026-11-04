"""Week 1 Day 6 Daily Challenge: Dictionaries, conditionals, and loops."""


def challenge_1():
    """Map each character in a user-supplied word to all its positions."""
    word = input("Enter a word: ")
    letter_indices = {}
    for index, letter in enumerate(word):
        if letter in letter_indices:
            letter_indices[letter].append(index)
        else:
            letter_indices[letter] = [index]
    print(letter_indices)
    return letter_indices


def challenge_2(items_purchase, wallet):
    """Buy affordable items in dictionary priority order, then sort the basket."""
    money = int(wallet.replace("$", "").replace(",", ""))
    basket = []
    for item, price in items_purchase.items():
        item_price = int(price.replace("$", "").replace(",", ""))
        if item_price <= money:
            basket.append(item)
            money -= item_price
    result = sorted(basket) if basket else "Nothing"
    print(result)
    return result


if __name__ == "__main__":
    print("Challenge 1: Letter Index Dictionary")
    challenge_1()

    print("\nChallenge 2: Affordable Items")
    items_purchase = {
        "Water": "$1",
        "Bread": "$3",
        "TV": "$1,000",
        "Fertilizer": "$20",
    }
    wallet = "$300"
    challenge_2(items_purchase, wallet)
