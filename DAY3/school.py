def student_details(n):
    students=[]
    for i in range(n):
        name=input("Enter name of student ")
        marks=int(input(f"Enter marks of {name} "))
        students.append((name,marks))
        highest=max(students,key=lambda x:x[1])
        print(f"Student with highest marks {highest[0]} ({highest[1]})")
        print("Students who scored above 75 ")
        for student in students:
            if student[1]>75:
                print(f"{student[0]} ({student[1]})")
x=int(input("Enter no of students "))
student_details(x)