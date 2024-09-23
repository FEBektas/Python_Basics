from art import logo
print(logo)

dict = {  # ---- a dictionary to identify the user response.
    1 : "Millimeters to Inches",
    2 : "Centimeters to Feet",
    3 : "Meters to Yards",
    4 : "Kilometers to Miles"
}

for key, value in dict.items():  # ---- print the dictionary on different lines.
    print(f"{key}-{value}")


# defined a function to express the logic and math behind the convertor.
def q1():
    while True: # ---- Loop for if the statement is higher than 4.
        convert_question = int(input("\nFrom the following available measurements units,"
                             " please tell me what do you wish to convert to!  "))
        if convert_question > 4:
            print(f"More convert units coming soon.")
            for key, value in dict.items():  # ---- print the dictionary on different lines.
                print(f"{key}-{value}")
        else:
            break
    number = int(input("Please enter what amount do you want to convert!  "))

    if convert_question == 1:
        inches = round(number / 25.4, 2) # ---- Rounding to 2 decimals
        print(f"Your conversion from {number} mm is {inches} inches")
    elif convert_question == 2:
        feet = round(number / 30.48, 3)  # ---- Rounding to 3 decimals
        print(f"Your conversion from {number} cm is {feet} feet")
    elif convert_question == 3:
        meters = round(number * 1.09361, 4) # ---- Rounding to 4 decimals
        print(f"Your conversion from {number} m is {meters} yards")
    elif convert_question == 4:
        kilometers = round(number * 0.621371, 5) # ---- Rounding to 5 decimals
        print(f"Your conversion from {number} km is {kilometers} miles")

q1() # ---- call the function.

while True:  # ---- To restart the convertor anytime the user agrees.
    another_convert = input("Do you want to do another conversion? (Yes/No)\n ").lower()
    if another_convert == "yes" or another_convert == "y":
        for key, value in dict.items():  # ---- print the dictionary on different lines.
            print(f"{key}-{value}")
        q1()
    else:
        break
print("See you soon!  ")