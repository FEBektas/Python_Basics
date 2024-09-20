from itertools import count

from art import logo

print(logo)

quote_question = input("Tell me your favorite quote!  \n").lower() # ---- User input for a favorite quote.
# print(quote_question)

vowels1 = "aeiou"

counter = 0  # ---- Starting te count from 0 to increment the number of vowels
#print(count)

quote_letters = len(quote_question) # Counting how many characters are in the user input.
# print(quote_letters)


for element in quote_question: # ---- The forloop where it finds the vowels and increments the count by one!
    if element in vowels1:
        counter += 1
two_dec_part = round(counter / quote_letters * 100, 2)
# print(two_dec_part)

print(f"From a total of {quote_letters} characters, there are {counter} vowels in your favorite quote!\n"
      f"There are a {two_dec_part}% of vowels in your quote!  ") # ---- The print statement with formated strings!




