#44 Programming questions Code
#Easy questions:
#5) An MxN size array is filled with random integers. Check if any cell in the array is 0 and set all the cells in that cell's row and column to O.

print("44 Programming questions Code - Easy 5\nhttps://github.com/xsenemy/44-programming-questions\n")

import random


mxn_array = [[],[],[]]
for i in mxn_array:
    for j in range(3):
        i.append(random.randint(0, 10))
    print(i)

print()

for i in range(len(mxn_array)):
    for j in mxn_array[i]:
        if j == 0:
            n = mxn_array[i].index(j)
            mxn_array[i][n] = "X"
for i in mxn_array:
    if "X" in i:
        n = i.index("X")
        for j in range(len(mxn_array)):
            i[j] = 0
            mxn_array[j][n] = 0

for i in mxn_array:
    print(i)

print("\nez")
