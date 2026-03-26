#Exercise 1: Hello World
# Print the following output using one line of code:

print("Hello world\n" * 4)

#Exercise 2: Some Math
#Write code that calculates the result of:

#(99^3)*8 (meaning 99 to the power of 3, times 8).
print((99**3)*8)


#Exercise 3: What is the output?
#Predict the output of the following code snippets:
#Comment what is your guess, then run the code and compare

15 < 8 #False
5 < 3 #False
3 == 3 #True
3 == "3" #False
"3" > 3 #False
"Hello" == "hello" #False


#🌟 Exercise 4: Your computer brand
#Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable, print a sentence that states the following:
#"I have a <computer_brand> computer."

computer_brand= "Dell"
print(f"I have a {computer_brand} computer")



#🌟 Exercise 5: Your information

#Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
#Have your code print the info message.
#Run your code.

name = "Avi"
age = "41"
shoe_size = "41"
info = (f" My name is {name}, I am {age} years old, my shoe size is {shoe_size}")
print (info)


#🌟 Exercise 6: A & B
#Create two variables, a and b.
#Each variable’s value should be a number.
#If a is bigger than b, have your code print "Hello World".

a = 2
b = 1
if a > b:
    print("Hello World")


#Exercise 7: Odd or Even
#Write code that asks the user for a number and determines whether this number is odd or even.

user_input = input("Enter an integer: ")
number = int(user_input)
if number % 2 == 0:
    print(f"The number {number} is Even.")
else:
    print(f"The number {number} is Odd.")

#🌟 Exercise 8: What’s your name?
#Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

user_name = input("Enter your name:")
name= "Avi"
if user_name == name:
    print("Cool, also my name is Avi")
else:
    print (f"Nice to meet with you {user_name}")

#🌟 Exercise 9: Tall enough to ride a roller coaster
#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.
user_height = int(input("Please write how long you are in cms?"))

if user_height > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.")