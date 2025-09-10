def del_specified(n):
    nums=[]
    for i in range(n):
        num=int(input("Enter values "))
        nums.append(num)
    pos=int(input("Enter position "))
    if pos<0 or pos>=len(nums):
        print("Invalid position ")
    else:
        for i in range(pos,len(nums)-1):
            nums[i]=nums[i+1]
        nums.pop()
        print("List after deletion: ",nums)
x=int(input("Enter no of elements "))
del_specified(x)
