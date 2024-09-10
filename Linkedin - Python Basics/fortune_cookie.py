# Fortune Cookie

# 1-Importing the Random Module:
# To use random numbers, you need to import the random module.
# Syntax: import random

# 2-Generating Random Integers:
# Use random.randint(min, max) to generate a random integer between min and max (inclusive).
# Example:
# python
# import random
# random_number = random.randint(1, 10)
# print(random_number) # Prints a random number between 1 and 10

# 3-Generating Random Floats:
# Use random.random() to generate a random float between 0 and 1.
# Example:
# python
# import random
# random_float = random.random()
# print(random_float) # Prints a random float between 0 and 1

# 4-Practical Use:
# Random numbers are useful for creating unpredictable outcomes, such as in games or simulations.


import random
from traceback import print_tb


# my approach

eight_ball = ("yes", "no", "maybe")
print(random.choice(eight_ball))

# tutorial approach

answer = random.randint(1,4)

if answer == 1:
    print("yes!")
elif answer == 2:
    print("no!")
elif answer == 3:
    print("maybe!")
else:
    print("I dont understand!")



# Choosing what fortune to show.

# 1-Importing the Random Module:
# To use random numbers, you need to import the random module.
# Syntax: import random

# 2-Generating a Random Lucky Number:
# Use random.randint(1, 100) to generate a random integer between 1 and 100.
# Example:
# python
# import random
# lucky_number = random.randint(1, 100)
# print(f"Your lucky number is {lucky_number}")

# 3-Creating Different Fortunes:
# Use random.randint(1, 3) to pick a random number between 1 and 3.
# Based on this number, use if statements to assign different fortunes.
# Example:
# python
# fortune_number = random.randint(1, 3)
# if fortune_number == 1:
# fortune_text = "You will have a great day!"
# elif fortune_number == 2:
# fortune_text = "Today will be tough, but worth it."
# else:
# fortune_text = "You will get married this year."
# print(fortune_text)

# 4-Combining Fortunes and Lucky Numbers:
# Use an f-string to combine the fortune text and lucky number.
# Example:
# python
# print(f"{fortune_text} Your lucky number is {lucky_number}")

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = ""

if fortune_number == 1:
    fortune_text = "You are unlucky, try again?"
elif fortune_number == 2:
    fortune_text = "In order to win you need to buy a coca-cola bottle!"
elif fortune_number == 3:
    fortune_text = "You are the lucky winner, CONGRATULATIONS!"

print(f"{fortune_text} Your lucky number is: {fortune_number}")
