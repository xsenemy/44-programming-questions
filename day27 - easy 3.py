#44 Programming questions Code
#Easy questions:
#3) Given an integer array of size 10, check if the integers are in ascending order, descending order, or neither.
import random

print("44 Programming questions Code - Easy 3\nhttps://github.com/xsenemy/44-programming-questions\n")


def make_list():
    for i in range(10):
        list.append(i)

list = []
case = random.randint(0, 2)
if case == 0:
    make_list()
elif case == 1:
    make_list()
    list.reverse()
elif case == 2:
    make_list()
    list[2], list[8] = list[8], list[2]

print(list)
list_type = 0
for i in range(len(list)-1):
    if list[i] < list[i+1]:
        list_type += 1
    elif list[i] > list[i+1]:
        list_type -= 1
if list_type == 9:
    print("List is in ascending order")
elif list_type == -9:
    print("List is in descending order")
else:
    print("List is in shuffled order")
