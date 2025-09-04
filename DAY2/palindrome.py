def palindrome(n):
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            print(i)
x = int(input("Enter a number: "))
palindrome(x)