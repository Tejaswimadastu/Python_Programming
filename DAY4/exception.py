def Exception_handling(x,y):
    try:
        z=x/y
        print(f"Divison of {a} and {b} is ",z)
    except:
        print("Error: Division by zero is not allowed")
a=int(input("Enter a number "))
b=int(input("Enter a number "))
Exception_handling(a,b)
