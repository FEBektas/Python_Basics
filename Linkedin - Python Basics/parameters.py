# Parameters are variables that you can pass into a function to provide it with specific information.
# They allow functions to be more flexible and reusable by using different inputs.
# When you define a function, you can specify parameters inside the parentheses.

pers_name = input("State your name!")

def hello(name):
    print(f"Hello {name}")

hello(pers_name)


number_1 = input("Choose a number")
number_2 = input("Choose another number")

def add_numbers(number_1, number_2):
    print(int(number_1) + int(number_2))

add_numbers(number_1,number_2)


# Exercise

animal_info = input("What animal do you have?")

def info(animal_info):
    print(f"Your {animal_info} is beautiful!") # ----- to make it more interactive add more conditional functions!

info(animal_info)