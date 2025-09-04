def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

def strong_numbers(n):
    for num in range(1, n + 1):
        temp = num
        s = 0
        while temp > 0:
            digit = temp % 10
            s += factorial(digit)
            temp //= 10
        if s == num:
            print(num, end=' ')

x = int(input("Enter n: "))
strong_numbers(x)