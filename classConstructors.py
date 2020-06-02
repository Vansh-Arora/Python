class Emp:
    #__init__ method in python is same as a constructor in java
    def __init__(self,fname,lname,sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal
    #Each fuction inside a class takes an argument self because whenever we call a class function an instance is always passed 
    def fullName(self):
        return '{} {}'.format(self.fname, self.lname)

emp1 = Emp(input("Enter first name: "),input("Enter last name: "),int(input("Enter salary: ")))
emp2 = Emp(input("Enter first name: "),input("Enter last name: "),int(input("Enter salary: ")))
print(emp1.sal)
print(emp1.fullName())
print(Emp.fullName(emp2))

