class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee details\nName ",self.name," Salary ",self.salary)
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def display(self):
        super().display()
        print("Department:", self.department)
obj=Manager("Teju",150000,"CSE")
obj.display()
obj=Employee("Hananya",300000)
obj.display()