def even_odd(n):
    nums=[]
    e=0
    o=0
    for i in range(n):
        num=int(input("Enter value "))
        nums.append(num)
        if num%2==0:
            e=e+1
        else:
            o=o+1
    print("Even count ",e," Odd count ",o)
x=int(input("Enter no of elements "))
even_odd(x)