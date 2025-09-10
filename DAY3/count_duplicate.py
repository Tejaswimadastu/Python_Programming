def count_duplicate(n):
    nums=[]
    for i in range(n):
        num=int(input("Enter values "))
        nums.append(num)
    duplicates=0
    checked=[]
    for i in nums:
        if nums.count(i)>1 and i is not checked:
            duplicates+=1
            checked.append(i)
    print("Number of duplicates ",duplicates)
x=int(input("Enter number of elements "))
count_duplicate(x)
