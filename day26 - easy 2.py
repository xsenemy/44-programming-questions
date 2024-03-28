#44 Programming questions Code
#Easy questions:
#2) Find all the prime factors of a positive integer entered by the user.

print("44 Programming questions Code - Easy 2\nhttps://github.com/xsenemy/44-programming-questions\n")


def prime_factorization(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)


n = int(input("Int: "))
prime_factorization(n)
