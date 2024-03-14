# 44 Programming questions Code
# Ultra easy questions:
#6) Utilizing the modulus operator, label all the even and odd numbers from 0-100. Do it again without the modulus
# operator. And a third time without using if/else/switch. (Note: 99.5% of programming job applicants. and 80% of /g/,
# will fail here)
from os import system, name

def clear():
    if name == "nt":
        return system("cls")
    return system("clear")

# %
input("press key for %")

for i in range(101):
    if i % 2 == 0:
        print(f"{i} even")
    else:
        print(f"{i} odd")

# !%
input("press key for !%")
clear()

n = 0
x = 1
for i in range(51):
    print(f"{n} even")
    if x != 101:
        print(f"{x} odd")
    n = x + 1
    x += 2

# !if/else/switch
input("press key for !if/else/switch")
clear()

even_list = []
odd_list = []
for i in range(0, 101, 2):
    even_list.append(i)
for i in range(1, 100, 2):
    odd_list.append(i)
for i in range(50):
    print(f"{even_list[i]} even")
    print(f"{odd_list[i]} odd")
print("100 even")
input("press key for quit")
