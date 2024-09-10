# 1-What is input?
# The input function allows users to interact with your Python program by entering data.
# Syntax: input("Your prompt message here")


# 2-Storing Input in a Variable:

# You can store the user's input in a variable for later use.

# Example:
# python
# user_text = input("Enter some text: ")
# print(user_text)

# This will prompt the user to enter text, which is then stored in user_text and printed.


# 3-Manipulating Input:

# You can manipulate the input data, such as converting it to uppercase.

# Example:
# python
# user_text = input("Enter some text: ")
# print(user_text.upper())

# This will print the user's input in uppercase.


# 4-Handling Numbers:

# Input is always received as a string. To use it as a number, you need to convert it.

# Example:
# python
# user_number = int(input("Enter a number: "))
# print(user_number * 2)

# This converts the input to an integer and then doubles it.


# user_information = input("Can you tell me more about yourself? ").upper()
#
# if user_information:
#     print(f"{user_information}, Nice new information!")
#
#
#
# user_number = input("What do you want to double? ")
#
# print(int(user_number) * 2) # ----- to transform the string into a int, just set int(the variable).



# Exercise - ask for some text and make it either upper or lower.

text = input("Can you provide me some text?  ")
low_or_upp = input("For upper select 1,\nand for lower select 2.  ") # ---- \n for a new row.
number_1 = 1
number_2 = 2

# Don't forget to transform the string into and int.
# input = allways string type.

if int(low_or_upp) == number_1:
    print(text.upper())
elif int(low_or_upp) == number_2:
    print(text.lower())
else:
    print("nothing!")






