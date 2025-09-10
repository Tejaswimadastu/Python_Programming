def unique(n):
    nums=[]
    for i in range(n):
        num=int(input("Enter values "))
        nums.append(num)
    for i in nums:
        if nums.count(i)==1:
            print(i,end=' ')
x=int(input("Enter number of elements "))
unique(x)