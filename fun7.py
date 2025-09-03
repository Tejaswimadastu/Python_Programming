def operations(x,y):
    c1=x+y
    c2=x-y
    c3=x*y
    c4=x/y
    c5=x%y
    return c1,c2,c3,c4,c5;
a=15
b=5
z=operations(a,b)
print("Operations\n1.add\n2.sub\n3.mul\n4.div\n5.mod\n",z)