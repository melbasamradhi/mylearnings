class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def display(self):
        print("I am in module1")
        print("E-Id:{} Name:{} Salary:{}".format(self.id,self.name,self.salary))




