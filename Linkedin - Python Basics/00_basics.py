# variables - Variables are like containers that store information which can change over time. Think of them as
# labels you can attach to different pieces of data. Variables can hold various types of data, such as numbers,
# text (strings), and even more complex types like booleans (True/False values).


# naming: You give a variable a name to identify it. For example, wallet can be a variable name. Assigning a Value:
# To assign a value to a variable, you use the equal sign =. For instance, wallet = 41 means the variable wallet now
# holds the value 41.

Wallet = 41

print(Wallet)

Wallet = 32

print(Wallet)



# ints and Floats Math Operations: You can perform various mathematical operations with both ints and floats,
# such as addition (+), subtraction (-), multiplication (*), and division (/).


# ints (integers) - Integers are whole numbers without any decimal points. They can be positive or negative.

day = 2

temp = -15

# floats -  Floats are numbers that have decimal points. They can also be positive or negative.

weight = 63.232 # floats can be positive or negative just like int.

print(weight - 0.2)

height = 164.50
age = 21



# strings - are sequences of characters used to represent text in Python. They are enclosed in quotes.
# Creating Strings: Double Quotes: You can use double quotes to create a string. You can also use single quotes.
# Consistency: You must start and end a string with the same type of quote.
# Using Different Quotes: If your string contains a single quote, use double quotes to enclose it.
# Escape Characters: Use a backslash \ to include quotes inside a string.

shirt = "white"

store = 'Pizza\'s Hut, the best there is' # if any time you want to have a quote you can put a backslash in front.

print(store)

movie = "DeadPool & Wolverine"



# F-strings (formatted string literals) allow you to embed expressions inside string literals, using curly braces {}.
# Syntax: Start the string with an f before the opening quote.

day_name = "Monday"
day = 2
date = "September"

print(f"Today's {day_name}, {date} {2}")



# Booleans and if statements
# Booleans represent a true or false value.
# If statements allow your code to make decisions based on conditions.

today_is_monday = True

if today_is_monday:
    print("This is the start of the Week")
else:
    print("There is one more week before Monday!")

centimeters = 165

if centimeters >= 165:
    print("You are a big boy!")
else:
    print("You midget")

age = 17

if age >= 18:
    print("You are an adult")
else:
    print("You are a child")