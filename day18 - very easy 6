#44 Programming questions Code
#Very easy questions:
#6) Generate a list of 200 integers, each between 0-10. Order it by size ascending, then by size descending.
# Now order it by mode ascending, and mode descending. (Mode is the most frequently repeated number in a list).

import random


def frequency_sort(list):
    for i in list[0]:
        temp = 0
        for j in list[0]:
            if i == j:
                temp += 1
        list[1].append(temp)


numbers = [random.randint(0, 10) for i in range(200)]
ascending, descending = (numbers.copy() for i in range(2))

# ascending ordered list
for i in range(1, len(ascending)):
    for j in range(len(ascending)):
        if ascending[i] < ascending[j]:
            ascending[j], ascending[i] = ascending[i], ascending[j]
# descending ordered list
for i in range(1, len(descending)):
    for j in range(len(descending)):
        if descending[i] > descending[j]:
            descending[j], descending[i] = descending[i], descending[j]
# ascending_mode ordered list
ascending_mode = [ascending.copy(), []]
frequency_sort(ascending_mode)
for i in range(len(ascending_mode[0])):
    for j in range(len(ascending_mode[0])):
        if ascending_mode[1][i] < ascending_mode[1][j] or \
                ascending_mode[1][i] == ascending_mode[1][j] and ascending_mode[0][i] < ascending_mode[0][j]:
            ascending_mode[0][j], ascending_mode[0][i] = ascending_mode[0][i], ascending_mode[0][j]
            ascending_mode[1][j], ascending_mode[1][i] = ascending_mode[1][i], ascending_mode[1][j]
# descending_mode ordered list
descending_mode = [descending.copy(), []]
frequency_sort(descending_mode)
for i in range(len(descending_mode[0])):
    for j in range(len(descending_mode[0])):
        if descending_mode[1][i] > descending_mode[1][j] or \
                descending_mode[1][i] == descending_mode[1][j] and descending_mode[0][i] < descending_mode[0][j]:
            descending_mode[0][j], descending_mode[0][i] = descending_mode[0][i], descending_mode[0][j]
            descending_mode[1][j], descending_mode[1][i] = descending_mode[1][i], descending_mode[1][j]

print(f"numbers \t{numbers}", end="\n\n")
print(f"ascending\t{ascending}")
print(f"descending\t{descending}", end="\n\n")
print(f"asc mode\t{ascending_mode[0]}")
print(f"des mode\t{descending_mode[0]}")
