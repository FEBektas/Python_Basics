from art import logo

print(logo)

# variables for the inputs of the user.

addition = ["+", "add", "addition"]
subtraction = ["-", "sub", "subtraction"]
multiplications = ["*", "mult", "multiplication"]
division = ["/", "div", "division"]


# Print statements with personalized messages.

print(f"You can select from the following operations!\n\nAddition:{addition}\nSubtraction:{subtraction}\n"
      f"Multiplication:{multiplications}\nDivision:{division}\n")

print("-----------------------------------------------\n")


operation_question = input("What operations do you want to use?  ").lower()


#List of options for the user to choose from.
operations = addition + subtraction + multiplications + division


# definitions for the operations.

def add():
    print(f"Your Addition result is: {first_number + second_number}")
def subtract():
    print(f"Your Subtraction result is: {first_number - second_number}")
def multiplication():
    print(f"Your Multiplication result is: {first_number * second_number}")
def divide():
    if first_number and second_number != 0:
        result = first_number / second_number
        print(f"Your Division result is: {result}")
        # if result = 0:
        #     print()
    else:
        print("Can not divide by Zero!\nTry another number except Zero")

# Loop for showing the result of the operation based on the user input.

if operation_question in operations:

    # input for the numbers of the user.

    first_number = int(input("Choose the first number!  "))
    second_number = int(input("Choose the second number!  "))

    for element in addition:
        if operation_question == element:
            add()

    for element in subtraction:
        if operation_question == element:
            subtract()

    for element in multiplications:
        if operation_question == element:
            multiplication()

    for element in division:
        if operation_question == element:
            divide()

else:
     print("No more operations for now!\nAdding more operations soon!  ")

