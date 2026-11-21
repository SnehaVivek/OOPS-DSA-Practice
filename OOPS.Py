# Learning OOPS topics:

# Types of variables and methods
# Inheritance - reusability
# Polymorphism - data security
# Encapsulation - data hiding
# Abstraction
# Interface

# Class is a template/bluprint/prototype for creating objects
# For examples
class Email :
    # Attributes
    # Methods
    pass
e1=Email()
e2=Email()
print(e1)


# Using __init__ to initalize the class
# 3 types of constructor

# Non-Parametize function
class Employee:
    def __init__(self):
        self.salary=22000
        self.age=21
e1=Employee()
print(e1.__dict__)  # To get the output

# Paramtize Function
class Emp():
    def __init__(self,sal,age):
        self.salary=sal
        self.age=age
e1=Emp(300000,34)
print(e1.__dict__)

# Deafult
class Email:
    pass
e1=Email()
e2=Email()
print(e1)

# Method inside the class
class Employee:
    def __init__(self,sal,arg):
        self.salary =sal
        self.age =arg
# Atribute inside the class
    def display(self):
        print(f"Salary is {self.salary} and age is {self.age}")
e1=Employee(24000,21)
# Attribute outside the class
print(e1.salary)
# Updating the salary or the attribute the class
e1.salary=34000
print(e1.salary)
e2=Employee(378000,25)
e2.display()


# Build-in class function
class er:
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag
r1=er('Sneha',23)
r2=er('Adwitiya',21)
# Gives the particular data 
print(getattr(e1,'age'))
# To change the value or update the content
print(setattr(e2,'age',39))
# To delete the value from the data
delattr(e2,'age')
print(e2.__dict__)
# To change the value for conditions
print(hasattr(e2,'name'))


# Build-in class attributes
# __doc__ -
print(er.__doc__)
# __name__
print(er.__name__)
# __dict__
print(er.__dict__)
# __module__
print(er.__module__)


# isinstance() fuction - whether the object is the part of the class or not
class demo():
    pass
d1=demo()
print(isinstance(e1,Employee))
print(isinstance(d1,Employee))


# 3 types of methods:
# Instance method
# Class method
# Static method

# Class methods - To change the variable inside the class
class Employee:
    company_name="Google"
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    @classmethod
    def get_company_name(cls):
        cls.company_name='Microsoft'
        print(cls.company_name)
e=Employee('Roy',40000)
Employee.get_company_name()

# 2 types of Instances method
# Setter method :- set values of instance variables
# getter method :- get values of instance variabes
class new():
    def setname(self,name):
        self.name=name
    def getname(self):
        print("The name is:",self.name)
ei=new()
ei.setname(input("Enter the name:"))
print(ei.__dict__)

# Static method