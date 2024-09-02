# Odd or even calculator

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