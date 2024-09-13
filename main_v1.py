import random
from art import logo

characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","w","x","y","z"]

upper_characters = [x.upper() for x in [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","w","x","y","z"
]]

special_characters = [
    "!","@","#","$","%","%","^","&","*","<",">","/","_","_","-","?",":",";","{","}","[","]", "+","=","(",")"
]

numbers = ["0","1","2","3","4","5","6","7","8","9"]


print(logo)


# Initialized empty list
password = []

# Extract x characters from lists.
extracted_characters = random.sample(characters, k=random.randint(1,3))
extracted_upp_ch = random.sample(upper_characters, k=random.randint(2,5))
extracted_spec_ch = random.sample(special_characters, k=random.randint(1,2))
extracted_numbers = random.sample(numbers, k=random.randint(3,5))

# print(extracted_characters) # --- print statement for debug.


# Adding extracted characters to password list.
for e in extracted_characters:
    password.append(e)
for e in extracted_upp_ch:
    password.append(e)
for e in extracted_spec_ch:
    password.append(e)
for e in extracted_numbers:
    password.append(e)
# print(password) ---- print statement for debug

random.shuffle(password)

# Joining all elements without spaces.
result = "".join(password)
print(f"The password you requested is:\n{result}" )
