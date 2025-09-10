def length_str(str):
    c=0
    for _ in str:
        c=c+1
    return c
def my_compare(s1,s2):
    if s1==s2:
        return "Both are equal"
    elif s1>s2:
        return "First string is greater"
    elif s1<s2:
        return "Second string is greater"
def concat(s1,s2):
    return s1+s2
s1=str(input("Enter first string "))
s2=str(input("Enter second string "))
print("Length of ",s1," is ",length_str(s1))
print("Length of ",s2," is ",length_str(s2))
print("Comparison of both is ",my_compare(s1,s2))
print("Concatination of both is ",concat(s1,s2))

