#student details
roll=int(input("Enter student roll number "))
sname=str(input("Enter student name "))
m,p,ch=map(int,input("Enter 3 subject marks ").split())
tot=m+p+ch
total=tot/3
if total<50:
    grade='C'
elif total>=51 and total<=75:
    grade='B'
elif total>=71 and total<=80:
    grade='A'
elif total>80:
    grade='Distinction'
elif total<40:
    grade='Fail'
else:
    grade='Pass'
print("Total marks :",total)
print("Grade :",grade)

