def fun(n):
    total = 1
    for i in range(1, n + 1):
        print(i, end='')
        total *= i
        if i < n:
            print('*', end='')
    print(f'={total}')
x = int(input("Enter n to give natural sum: "))
fun(x)