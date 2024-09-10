import random
import time
print("Hello and wellcome to my guessing game.\nI'm going to choose a number between 1 and 100!\nGood luck!  ")
time.sleep(2)
print("Picking a number... ")
time.sleep(3)


correct_number = random.randint(0,100)
# print(correct_number)
guess = int(input("What is your guess?: "))
guess_count = 1

# Use while loop when you don't know how many times you need to loop

while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        print("You are low, choose a higher number!  ")
    else:
        print("You are too high, choose a lower number!  ")
    guess = int(input("What is your guess?: "))

print(f"Congrats! The right answer was {correct_number}.\nIt took you {guess_count} guesses  ")





