# TODO course problem number 5.
# Is there a remainder?

# Your task: Create a function named has_remainder() that takes two ints and divides the first number by the second
# number. Then the function should return True if there is a remainder. The function should return False if there is
# not a remainder.

# Personal approach.

def calc():
    number1 = 5
    number2 = 4
    if number1 % number2 == 0:
        return False
    else:
        return True
calc()


# Course solution.

def has_remainder(number1, number2):
    number1 = 5
    number2 = 4
    remainder = number1 % number2
    if remainder == 0:
        return False
    else:
        return True


has_remainder(number1=5, number2=4)
result = has_remainder(number1=5, number2=4)