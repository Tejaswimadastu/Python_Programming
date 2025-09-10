def count_str(str):
    alphabets=digits=special=0
    for i in str:
        if i.isalpha():
            alphabets=alphabets+1
        elif i.isdigit():
            digits=digits+1
        else:
            special=special+1
    return alphabets,digits,special
x=str(input("Enter a string "))
a, d, sp = count_str(x)
print("Alphabet count ",a)
print("Digits count ",d)
print("Special Characters count ",sp)

