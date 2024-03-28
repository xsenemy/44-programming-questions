#44 Programming questions Code
#Easy questions:
#2) Find all the prime factors of a positive integer entered by the user.

print("44 Programming questions Code - Easy 2\nhttps://github.com/xsenemy/44-programming-questions\n")


def prime_factorization(n):

    for i in range(2, n+1):
        if n % i == 0:
            prime = True
            for j in range(2, int((i**0.5)+1)):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                print(f"{n} / {i}")
                prime_factors.append(i)
                prime_factorization(n=int(n / i))
                break

n = int(input("Int: "))
prime_factors = []
prime_factorization(n)
print("Prime factors: ")
print(*prime_factors, sep=" x ")
