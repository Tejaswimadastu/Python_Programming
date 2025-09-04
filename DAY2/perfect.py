def perfect(n):
    k=n
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==k:
        print("Perfect number ")
    else:
        print("Not a perfect number ")
x=int(input("Enter a number "))
perfect(x)
