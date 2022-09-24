import random
from let_num_sym import *

print("Welcome to the PyPassword Generator!\n")

nr_letters= int(input("How many letters would you like in your password?\n")) 
random_letters = random.choices(letters, k=nr_letters)
# print(random_letters)

nr_symbols = int(input(f"How many symbols would you like?\n"))
random_symbols = random.choices(symbols, k=nr_symbols)
# print(random_symbols)

nr_numbers = int(input(f"How many numbers would you like?\n"))
random_numbers = random.choices(numbers, k=nr_numbers)
# print(random_numbers)

combine_letnumsym = random_letters + random_symbols + random_numbers
# print(type(combine_letnumsym))

randomized_letnumsym = random.sample(combine_letnumsym, len(combine_letnumsym))
# print(randomized_letnumsym)
# print(type(randomized_letnumsym))

new_password = ''.join(randomized_letnumsym)

print(f"\nYour password is: {new_password}")