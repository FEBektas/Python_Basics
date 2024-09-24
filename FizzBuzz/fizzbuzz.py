from art import logo
import time
print(logo)

print("Wellcome to my FizzBuzz game!  ")
time.sleep(1)



def q1():
    fizzbuzz_counter = 0
    fizz_counter = 0
    buzz_counter = 0
    number_counter = higher_number - fizzbuzz_counter - fizz_counter - buzz_counter
    # number_percentage = round(number_counter / higher_number * 100, 2)
    for i in range(1, higher_number + 1):
        if i % 5 == 0 and i % 3 == 0:
            fizzbuzz_counter += 1
            print("FizzBuzz")
        elif i % 3 == 0:
            fizz_counter += 1
            print("Fizz")
        elif i % 5 == 0:
            buzz_counter += 1
            print("Buzz")
        else:
            print(i)
    fizzbuzz_percentage = round(fizzbuzz_counter / higher_number * 100, 2)
    fizz_percentage = round(fizz_counter / higher_number * 100, 2)
    buzz_percentage = round(buzz_counter / higher_number * 100, 2)
    print(f"That's it, you've got a grasp of the game!\n"
          f"At the end there are {fizzbuzz_counter} FizzBuzzes, {fizz_counter} Fizz's, {buzz_counter} Buzz's "
          f"and {number_counter} numbers!\n"
          f"And the percentage is: {fizzbuzz_percentage}% of FizzBuzz's,"
          f" {fizz_percentage}% Fizz's and {buzz_percentage}% Buzz's!")

while True:
    higher_number = int(input("In order to proceed, you will need to choose a number higher or equal to 20!  "))
    if higher_number < 20:
        time.sleep(1)
        print("Like I sayed, you need to choose a number higher or equal to 20!  ")
        time.sleep(1)
    else:
        q1()
        break
# print(user_number)

# while True: # loop if the player wants to select more numbers.
#     second_choice = input("Do you want to choose another number?  (yes/no) ").lower()
#     if second_choice == "yes" or second_choice == "y":
#         user2_number = int(input("In order to proceed, choose a number above 20! "))
#         time.sleep(1)
#         user_number = int(input("Choose another number above 20!  "))


