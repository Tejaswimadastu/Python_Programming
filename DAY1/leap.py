def leap(n):
    if (n%100!=0 and n%4==0) or (n%100==0 and n%4==0 and n%400==0):
        print(f"The leap year is {n}")
    else:
        print("Not a leap year")
leapy=int(input("Enter year "))
leap(leapy)

