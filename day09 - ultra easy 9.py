#44 Programming questions Code
#Ultra easy questions:
#9) Generate three random integers, each between 0-20. Find the largest, smallest, and average of the three.

import random

numbers = []
for i in range(3):
    numbers.append(random.randint(0, 20))

print(numbers)
print(f"largest: {max(numbers)}", f"smallest: {min(numbers)}", f"average: {sorted(numbers)[1]}")
