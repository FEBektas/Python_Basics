# Returning Values: The return statement allows a function to send back a value to the place where it was called.
# This is useful for using the result of a function elsewhere in your code.


# 1-Defining a Function:

# Example:
# python
# def double(number):
# return number * 2

# Here, the function double takes a parameter number and returns that number multiplied by 2.

# 2- Calling the Function:

# Example:
# python
# result = double(5)
# print(result) # Outputs: 10

# When you call double(5), it returns 10, which is then stored in the variable result and printed.


def double(number):
    return number * 10

new_number = double(5)



# Exercise - return the string in all caps.

question = input("Write anything you want!").upper()

def rand_string(question):
    return question
print(question)


names = ["alex", "erkan", "george", "andrei"]

for name in names:
    print(name.upper())

