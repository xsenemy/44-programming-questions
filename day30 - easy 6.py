#44 Programming questions Code
#Easy questions:
#6) Let the user enter an integer "n", then calculate "n" factorial (n!). Impose whatever limits on "n" that you feel necessary. (5! = 	5*4*3*2*1).

print("44 Programming questions Code - Easy 6\nhttps://github.com/xsenemy/44-programming-questions\n")

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

n = int(input("n (1 - 10): "))
while n < 1 or n > 10:
    n = int(input("n (1 - 10): "))
print(factorial(n))
