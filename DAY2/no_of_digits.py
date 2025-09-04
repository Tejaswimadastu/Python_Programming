def num_of_digits(n):
    s=0
    c=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
        c=c+1
    print(c)
x=int(input("Enter a number "))
num_of_digits(x)