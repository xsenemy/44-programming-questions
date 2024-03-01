#44 Programming questions Code
#Ultra easy questions:
#11) Generate a list of 100 random integers, each between 0-10000. Enter a number and check if it is in the list.

import random

list_of_numbers = []
for i in range(100):
    list_of_numbers.append(random.randint(0, 10000))

print(list_of_numbers)
check = int(input("Enter a number: "))
if check in list_of_numbers:
    print("It's on the list")
else:
    print("Not on the list")
