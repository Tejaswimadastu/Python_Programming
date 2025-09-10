def frequency(n):
    nums = []
    for i in range(n):
        num = int(input("Enter values "))
        nums.append(num)
    checked = []
    for i in range(n):
        if nums[i] not in checked:
            count = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1
            print(f"{nums[i]} -> {count}")
            checked.append(nums[i])

x = int(input("Enter number of elements "))
frequency(x)