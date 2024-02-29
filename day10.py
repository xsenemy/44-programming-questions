# 44 Programming questions Code
# Ultra easy questions:
#10) For a certain school class, you are given one test and an optional project. For the test. if you score below 50
# (out of a 100). you get an F. 50-69 is C, 70-89 is B, and 90-100 is A. If you submit the optional project, you raise
# your grade by one letter. Let the user input their marks (0-100) and 	whether they submitted the project (Y/N), and
# give them their grade.

#DIFFICULTY INCREASED: DON'T USE IF STATEMENT

def graduation(grade):
    while user_grade not in grade:
        return True
    return False

user_grade = int(input("insert the grade (0-100): "))
project = input("project? y/n: ")

f = []
c = []
b = []
a = []
grades = [f, c, b, a]
grades_dict = {
    0 : "f",
    1 : "c",
    2 : "b",
    3 : "a",
    4 : "a",
    "y" : 1,
    "n" : 0,
}

for i in range(50):
    f.append(i)
for i in range(50, 70):
    c.append(i)
for i in range(70, 90):
    b.append(i)
for i in range(90, 101):
    a.append(i)

n = 0
while graduation(grades[n]):
    n += 1

final_grade = n + grades_dict[project]

print(f"Your grade is: {grades_dict[final_grade]}")

