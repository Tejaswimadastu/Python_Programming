#student details
roll=int(input("Enter student roll number "))
sname=str(input("Enter student name "))
m,p,ch=map(int,input("Enter 3 subject marks ").split())
total=m+p+ch
avg=total/3
print("Roll number ",roll)
print("Student name ",sname)
print("Total marks ",total)
print("Average marks ",round(avg,2))