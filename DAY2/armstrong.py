def armstrong_numbers(n):
    for num in range(1, n + 1):
        temp = num
        s = 0
        digits = len(str(num))
        while temp > 0:
            r = temp % 10
            s += r ** digits
            temp //= 10
        if s == num:
            print(num, end=' ')

x = int(input("Enter n: "))
armstrong_numbers(x)