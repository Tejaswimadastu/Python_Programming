def remove_duplicate(n):
    nums=[]
    for i in range(n):
        num=int(input("Enter values "))
        nums.append(num)
        nums=list(set(nums))
    print("Without duplicates ",nums)
x=int(input("Enter no of elements "))
remove_duplicate(x)