# Exercise 1
# - Print all even numbers from 1 to 20:
    # - Expected Result: 2 4 6 8 10 12 14 16 18

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16 ,17 ,18 ,19 ,20]



for n in numbers:
    if n % 2 == 0:
         print(n)

# second approach.

for x in range(21):
    # if x % 2 == 0:
       print(x)



# - Calculate the factorial of a given number (e.g., 5):
#     - Expected Result: 120

# Hardcode data set.

number = [1, 2, 3, 4, 5] # ---- for sum you allways start with 0 and for the fact you start with 1

fact = 1

for n in number:
   fact *= n
print(fact)


# Interactive factorial calculator based on the user input.

user_selection = input("Enter a number")
integer = int(user_selection) # - Transformed the string into an int.

fact = 1

for n in range(1, integer):
    fact *= n
print(fact)


# - Print the elements of a list in reverse order:
    # - List: [10, 20, 30, 40, 50]

# First approach.

elements = [10, 20, 30, 40, 50]

rever_ele = elements[::-1]
print(rever_ele)

# Second approach.

elements = [10, 20, 30, 40, 50]

elements.reverse()
print(elements)


# - Print the first 10 Fibonacci numbers:
    # - Expected Result: 0 1 1 2 3 5 8 13 21 34

# n = 01


# Practice exercises.

# Print elements of a data set x times.

AnimalList = ['Cat','Dog','Tiger','Cow']
for x in AnimalList:
    for n in range(20):
        print(x)



# Nested conditional statement.

flowers = ['Jasmine','Lotus','Rose','Sunflower']
for f in flowers:
    print(f)
    if len(f) >= 5:
        print("The flowers smell nice")
    elif len(f) <= 5:
        print("This is a beautiful flower")
else:
    print("No more flowers!")



# Print elements of 2 combined data sets x times.

list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']

for x in list1:
    for y in list2:
        print(x, y)



# Using break statement inside a for loop in Python.

vehicles = ['Car','Cycle','Bus','Tempo']

for v in vehicles:
    if v == "car":
        break # ---- Using break will print the list stopping at the condition.
    print(v)



# Using continue statement inside a for loop in Python.

vehicles = ['Car','Cycle','Bus','Tempo']

for v in vehicles:
    if v == "Bus":
        continue # ---- Using continue will print the list with only the condition out.
    print(v)



# Python for loop to count the number of elements in a list.

numbers = [12, 3, 56, 67, 89, 90]

for n in range(1):
    print(len(numbers))



# Python for loop to find the multiples of 5 in a list

numbers = [2,5,6,10,15,20,25]

for n in numbers:
    if n%5 == 0:
        print(n)
