def divisible5or11(n):
    if n%5==0 and n%11==0:
        print("Divisible by 5 and 11 ")
    elif n%5==0:
        print("Divisible by 5 ")
    elif n%11==0:
        print("Divisible by 11")
    else:
        print("Not divisile by 5 and 11")

x=int(input("Enter a number "))
divisible5or11(x)