# Odd or even calculator

# 1-Modulo Operator:
# The % operator (modulo) gives the remainder of a division.
# Example: 7 % 2 equals 1 because 7 divided by 2 is 3 with a remainder of 1.

# 2-Check Remainder:
# If the remainder when dividing by 2 is 0, the number is even.
# If the remainder is 1, the number is odd.

# 3-Using If Statements:
# Use an if statement to check the remainder.

# Modulo Operator: number % 2 gives the remainder of number divided by 2.
# If Statement: Checks if the remainder is 1 (odd) or 0 (even).


# Solution 1
from math import remainder


def your_code():
    number = 7

    # Calculating remainder inside conditional statement.

    if number % 2:
        return False
        # print("This is an odd number")
    else:
        return True
        # print("This is an even number")



# Solution 2
your_code()

def test_code():
    number = 7

    # Calculate remainder before condition statements.

    var = number % 2

    if var == 1:
        return True
    else:
        return False

test_code()