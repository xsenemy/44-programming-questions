#44 Programming questions Code
#Very easy questions:
#12) Assume that you are retrieving an array of integers. This array has a size of 1000 and was supposed to be filled
# with all the unique integers from 0 to 999 in random order. Unfortunately, there was a problem with the person inputting
# the data, and we do not know if the array is actually full or not. We also know that one of the integers was repeated
# by mistake, while all the rest were unique. Find the repeated integer.

print("44 Programming questions Code - Very Easy 12\nhttps://github.com/xsenemy/44-programming-questions\n")

import random

#array generation, sometimes is not full
array = []
for i in range(1000-random.randint(0,1)):
    array.insert(random.randint(0, len(array)), i)
#mistake repeated int
n1 = random.randint(0, len(array)-1)
n2 = random.randint(0, len(array)-1)
while True:
    if array[n1] == array[n2]:
        n1 = random.randint(0, len(array) - 1)
        n2 = random.randint(0, len(array) - 1)
    else:
        array[n1] = array[n2]
        break

print(array)
if len(array) < 1000:
    print(f"The array is not full, {1000-len(array)} element is missing")
else:
    print("The array is full, every 1000 elements are present")

array2 = array.copy()
for i in array:
    n = i
    array2.remove(i)
    if n in array2:
        print(n)
        print(f"The nigger monkey put two equal ones integers, there are two {n} in the array.")
        break
