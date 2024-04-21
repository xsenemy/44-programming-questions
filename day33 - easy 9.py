#44 Programming questions Code
#Easy questions:
#9) Write an algorithm that plays the Towers of Hanoi with "n" disks.

print("44 Programming questions Code - Easy 9\nhttps://github.com/xsenemy/44-programming-questions\n")


def init_disks():
    # n_disks = int(input("How many disks?: "))
    n_disks = 5
    base_diameter = 5 * n_disks
    disks = []
    for i in range(n_disks):
        disks.append(base_diameter)
        base_diameter -= 5
    return disks


def move(x, y):
    try:
        if rods[x][-1] > rods[y][-1]:
            rods[x].append(rods[y].pop())
        else:
            rods[y].append(rods[x].pop())
    except IndexError:
        try:
            rods[x].append(rods[y].pop())
        except IndexError:
            rods[y].append(rods[x].pop())


def hanoi():
    for i in range(1, 2 ** len(disks)):
        if i % 3 == 1:
            move(0, 2)
        elif i % 3 == 2:
            move(0, 1)
        elif i % 3 == 0:
            move(1, 2)
        print(*rods)


disks = init_disks()
rods = [[] for i in range(3)]
rods[0] = [i for i in disks]
print(*rods, end="\n\n")

hanoi()
