#44 Programming questions Code
#Easy questions:
#5) An MxN size array is filled with random integers. Check if any cell in the array is 0 and set all the cells in that cell's row and column to O.

print("44 Programming questions Code - Easy 5\nhttps://github.com/xsenemy/44-programming-questions\n")

import random

m = 4
n = 4
mxn_array = []
for i in range(m):
    mxn_array.append([])
for i in mxn_array:
    for j in range(n):
        i.append(random.randint(0, 9))
    print(i)

print()

for i in range(len(mxn_array)):
    for j in mxn_array[i]:
        if j == 0:
            n = mxn_array[i].index(j)
            mxn_array[i][n] = "X"
for i in mxn_array:
    while "X" in i:
        x = i.index("X")
        i[x] = 0
        for j in range(len(i)):
            if i[j] != "X":
                i[j] = 0
            for k in mxn_array:
                if k[x] != "X":
                    k[x] = 0


for i in mxn_array:
    print(i)
    
