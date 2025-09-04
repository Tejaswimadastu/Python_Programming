def first_last(n):
    last = n % 10
    first = n
    while first >= 10:
        first = first // 10
    print("First", first, "last", last)
x = int(input("Enter a number: "))
first_last(x)