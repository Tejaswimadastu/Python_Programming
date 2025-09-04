def sum_digits(n):
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    print(s)
x=int(input("Enter a number "))
sum_digits(x)
