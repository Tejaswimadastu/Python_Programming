class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Student details\nStudent name ",self.name," Marks ",self.marks)
obj=Student("Teju",45)
obj.display()
obj=Student("Honey",50)
obj.display()