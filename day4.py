#44 Programming questions Code
#Ultra easy questions:
#4) Sum all the integers from 0 -> 1000. Sum all the integers from [x] -> [y], assuming that "x" is smaller than "y".

total = 0
total_r = 0

x = int(input("X value (smaller): "))
y = int(input("Y value (larger): "))

for i in range(1001):
    total += i
for i in range(x, y+1):
    total_r += i

print(f"sum from 0 to 1000: {total}")
print(f"sum from {x} to {y}: {total_r}")
