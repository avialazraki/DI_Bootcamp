#🌟 Exercise 1: Converting Lists into Dictionaries
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))
print(result_dict)

#🌟 Exercise 2: Cinemax #2
#Write a program that calculates the total cost of movie tickets for a family based on their ages.

#Family members’ ages are stored in a dictionary.
#The ticket pricing rules are as follows:
#Under 3 years old: Free
#3 to 12 years old: $10
#Over 12 years old: $15
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
print("--- Movie Ticket Prices ---")

# --- Loop Through Family Dictionary ---
for name, age in family.items():
    # --- Ticket Pricing Rules ---
    if age < 3:
        price = 0
        price_text = "Free"
    elif 3 <= age <= 12:
        price = 10
        price_text = "$10"
    else:
        price = 15
        price_text = "$15"

    total_cost += price
    print(f"{name.capitalize()} (Age {age}): {price_text}")

# --- Output Total ---
print("--------------------------")
print(f"Total Family Cost: ${total_cost}")
print("--------------------------\n")

print("--- Bonus: User Input ---")
custom_family = {}
while True:
    name = input("Enter family member name (or 'done' to finish): ").lower()
    if name == 'done':
        break
    try:
        age = int(input(f"Enter {name}'s age: "))
        custom_family[name] = age
    except ValueError:
        print("Please enter a valid number for age.")

# Calculate custom family cost
if custom_family:
    custom_total = 0
    print("\n--- Custom Ticket Prices ---")
    for name, age in custom_family.items():
        if age < 3:
            price = 0
        elif 3 <= age <= 12:
            price = 10
        else:
            price = 15
        custom_total += price
        print(f"{name.capitalize()}: ${price}")

    print("--------------------------")
    print(f"Total Custom Cost: ${custom_total}")
else:
    print("No family members added.")

#🌟 Exercise 3: Zara
#Create and manipulate a dictionary that contains information about the Zara brand.
brand = {
"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color": {
    "France": "blue",
    "Spain": "red",
    "US": ["pink", "green"]
    }
}
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 1. Change the value of number_stores to 2
brand["number_stores"] = 2

# 2. Print a sentence describing Zara’s clients
print(f"Zara sells clothing for: {', '.join(brand['type_of_clothes'])}.")

# 3. Add a new key country_creation with the value Spain
brand["country_creation"] = "Spain"

# 4. Check if international_competitors exists and add “Desigual”
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 5. Delete the creation_date key
del brand["creation_date"]

# 6. Print the last item in international_competitors
print(f"Last competitor: {brand['international_competitors'][-1]}")

# 7. Print the major colors in the US
print(f"US major colors: {brand['major_color']['US']}")

# 8. Print the number of keys in the dictionary
print(f"Number of keys: {len(brand)}")

# 9. Print all keys of the dictionary
print(f"Keys: {list(brand.keys())}")

#🌟 Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Map characters to their indices
char_to_index = {char: i for i, char in enumerate(users)}
print("1. Character to Index:", char_to_index)

# 2. Map indices to characters
index_to_char = {i: char for i, char in enumerate(users)}
print("2. Index to Character:", index_to_char)

# 3. Alphabetically sorted characters mapped to their ORIGINAL indices
# First, sort the list, then create the mapping
sorted_users = sorted(users)
sorted_char_to_index = {char: i for i, char in enumerate(sorted_users)}
print("3. Sorted Character to Index:", sorted_char_to_index)