#🌟 Exercise 1: Favorite Numbers

#Create a set called my_fav_numbers and populate it with your favorite numbers.
#Add two new numbers to the set.
#Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {3,5,7}
my_fav_numbers.add(4)
my_fav_numbers.add(6)
my_fav_numbers.remove(6)
friend_fav_numbers = {1,2,8}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our Favorites:", our_fav_numbers)


#🌟 Exercise 2: Tuple
#Given a tuple of integers, try to add more integers to the tuple.
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.


original_tuple = (1, 2, 3)
new_integers = (4, 5)
new_tuple = original_tuple + new_integers
print(f"Original tuple: {original_tuple}")
print(f"New tuple: {new_tuple}")

#🌟 Exercise 3: List Manipulation
#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
basket.remove("Banana")
#Remove "Blueberries" from the list.
basket.remove("Blueberries")
#Add "Kiwi" to the end of the list.
basket.add("Kiwi")
#Add "Apples" to the beginning of the list.
basket.insert(0, "Apples")
#Count how many times "Apples" appear in the list.
apple_count = basket.count("Apples")
print(f"Count of Apples: {apple_count}")
#Empty the list.
basket.clear()
#Print the final state of the list.
print(basket)


#🌟 Exercise 4: Floats
#Recap: What is a float? What’s the difference between a float and an integer?
#Create a list containing the following sequence of mixed types: floats and integers:
#1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
#Avoid hard-coding each number manually.
#Think: Can you generate this sequence using a loop or another method?

number_sequence = []
for i in range(15, 55, 5):
    number_sequence.append(i / 10.0)

print(number_sequence)


#🌟 Exercise 5: For Loop
#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 where the index is even.

print("Numbers from 1 to 20:")
for number in range(1, 21):
    print(number)


print("\nEven numbers from 1 to 20:")
for even_number in range(2, 21, 2):
    print(even_number)



#🌟 Exercise 6: While Loop

#Use an input to ask the user to enter their name.
#Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
#hint: check for the method isdigit()
#if the input is incorrect, keep asking for the correct input until it is correct
#if the input is correct print “thank you” and break the loop

while True:
    name = input("Enter your name: ")

    # Check if it's not digits and at least 3 characters long
    if not name.isdigit() and len(name) >= 3:
        print("thank you")
        break
    else:
        print("Invalid input. Please enter a valid name (at least 3 letters, not only numbers).")


#🌟 Exercise 7: Favorite Fruits
#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
#Store these fruits in a list.
#Ask the user to input the name of any fruit.
#If the fruit is in their list of favorite fruits, print:
#"You chose one of your favorite fruits! Enjoy!"
#If not, print:
#"You chose a new fruit. I hope you enjoy it!"

fruits_input = input("Enter your favorite fruits, separated by spaces: ")
favorite_fruits = fruits_input.split()
chosen_fruit = input("Enter the name of any fruit: ")
if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#🌟 Exercise 8: Pizza Toppings
#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print:
#"Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.

toppings = []
base_price = 10.00
topping_price = 2.50
prompt = "Enter a pizza topping (type 'quit' to finish): "

# Start the loop to get user input
while True:
    # Get user input
    topping = input(prompt)

    # Check for the 'quit' condition to break the loop
    if topping.lower() == 'quit':
        break
    # Check for empty input
    elif not topping.strip():
        print("Please enter a valid topping.")
    # Process the topping
    else:
        toppings.append(topping.strip().title()) # Store the topping
        print(f"Adding {topping.strip().title()} to your pizza.")

# After the loop, calculate the total cost
num_toppings = len(toppings)
total_cost = base_price + (num_toppings * topping_price)

# Print the final order summary
print("\n--- Your Pizza Order Summary ---")
if toppings:
    print("Toppings added:")
    for t in toppings:
        print(f"- {t}")
else:
    print("No toppings selected (plain pizza).")

print(f"Base price: ${base_price:.2f}")
print(f"Toppings cost ({num_toppings} @ ${topping_price:.2f} each): ${num_toppings * topping_price:.2f}")
print(f"Total cost: ${total_cost:.2f}")
print("Enjoy your pizza!")

#🌟 Exercise 9: Cinemax Tickets
#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.

# Initialize total cost
total_cost = 0

print("--- Movie Ticket Calculator ---")
print("Enter the age of each person.")
print("Type 'quit' when you are finished.\n")

while True:
    age_input = input("Enter age: ")

    # Allow user to exit the loop
    if age_input.lower() == 'quit':
        break

    try:
        # Convert input to integer
        age = int(age_input)

        # Apply pricing rules
        if age < 3:
            ticket_price = 0
            print("-> Free ticket (under 3)")
        elif 3 <= age <= 12:
            ticket_price = 10
            print("-> $10 ticket (3-12)")
        else:
            ticket_price = 15
            print("-> $15 ticket (over 12)")

        total_cost += ticket_price

    except ValueError:
        print("Invalid input. Please enter a number or 'quit'.")

# Final output
print(f"\nTotal ticket cost for the family: ${total_cost}")


#Bonus:
#Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
#Write a program to:
#Ask for each person’s age.
#Remove anyone who isn’t allowed to watch.
#Print the final list of attendees.

# 1. Ask for the number of people in the group
num_people = int(input("How many teenagers are in the group? "))

# Initialize an empty list to store ages
attendees = []

# 2. Ask for each person’s age
for i in range(num_people):
    age = int(input(f"Enter age of person {i+1}: "))
    attendees.append(age)

# Define restrictions
MIN_AGE = 16
MAX_AGE = 21

# 3. Remove anyone who isn't allowed (keep only 16-21)
# Using list comprehension to filter the list
final_list = [age for age in attendees if MIN_AGE <= age <= MAX_AGE]

# 4. Print the final list of attendees
print("\n--- Final List of Allowed Attendees ---")
print(final_list)
print(f"Total allowed: {len(final_list)}")