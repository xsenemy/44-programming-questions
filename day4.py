total = 0
total_r = 0

for i in range(1001):
    total += i
for i in range(100, 0, -1):
    total_r += i

print(f"sum from 0 to 1000: {total}")
print(f"sum from 100 to 0: {total_r}")
