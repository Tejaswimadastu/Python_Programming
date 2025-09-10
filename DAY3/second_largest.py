def second_largest(n):
    nums=[]
    for i in range(n):
        num=int(input("Enter values "))
        nums.append(num)
    nums=list(set(nums))
    nums.sort()
    if len(nums)<2:
        print("No second largest ")
    else:
        print("Second largest is ",nums[-2])
x=int(input("Enter number of elements "))
second_largest(x)