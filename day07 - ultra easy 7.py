# 44 Programming questions Code
# Ultra easy questions:
#7) Print the 12x12 multiplication table. (Challenge: Use only a single loop.)

#double loop
print("\ndouble loop\n")
for i in range(1, 13):
    n = ""
    for j in range(1, 13):
        n += str(i * j) + "\t\t"
    print(n)

#single loop
print("\nsingle loop\n")

def row(s):
    x = ""
    for i in range(1, 13):
        x += str(i * s) + "\t\t"
    return x

print(row(1), row(2), row(3), row(4), row(5), row(6), row(7), row(8), row(9), row(10), row(11), row(12), sep='\n')
