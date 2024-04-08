#44 Programming questions Code
#Easy questions:
#7) An array of size 100 is filled with random integers. Let the user pick an integer [x] between 0 and 98. Reverse the order of all the cells from [x]

print("44 Programming questions Code - Easy 7\nhttps://github.com/xsenemy/44-programming-questions\n")

import random

nums = []
ordered_nums = []
for i in range(100):
    nums.append(random.randint(0, 100))
int_x = 50
if int_x not in nums:
    print(nums)
    print(f"{int_x} not in list")
else:
    int_x_index = nums.index(int_x)
    for i in range(0, int_x_index + 1):
        ordered_nums.append(nums[i])
    n = 1
    for i in range(int_x_index + 1, len(nums)):
        ordered_nums.append(nums[-n])
        n += 1
    print(nums)
    print(ordered_nums)
