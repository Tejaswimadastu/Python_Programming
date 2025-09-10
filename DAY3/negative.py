def list_empty(n):
    nums = []
    for i in range(n):
        num = int(input("Enter value: "))
        nums.append(num)
    print("Negative numbers are:")
    for number in nums:
        if number < 0:
            print(number)
x = int(input("Enter number of elements: "))
list_empty(x)