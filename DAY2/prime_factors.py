def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(m):
    for i in range(2, m + 1):
        if m % i == 0 and is_prime(i):
            print(i, end=' ')

x = int(input("Enter n: "))
prime_factors(x)