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
class Employee :
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
class Employee :
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
class bank:
    bank_name='BOI'
    rate_of_interest =12.25
    @staticmethod
    def simple_interest(pin,n):
        si=(pin*n*bank.rate_of_interest)/100
        print(si)
float(input("Enter principal amount:"))
n=int(input("Enter number of years:"))
bank.simple_interest(200000,3)



# Inheritance
# Types Inheritance

# 1st
# Singles-level Inheritance
# Multi-level Inheritance
class father():                         # Single
    def __init__(self):
        print("father contructor called")
        self.vehicle='Scooter'
class son(father):
    def __init__(self):
        print("son contructor called")
        self.vehicle='BMW'
s=son()
print(s.__dict__)

# 2nd
# Hierarchical Inheritance - one parent mutilple child
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('The person',self.name)
class employee(person):
    def __init__(self,name,age,sal):
        super().__init__(name,age)
        self.salary=sal
    def display(self):
        print('This is employee')
class student(person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
    def display(self):
        print('This is student')

student1=student('What',18,100)
employee1=employee('vivek',23,240000)
student1.display()

# 3rd
# Multiple Inheritance
class country:
    def __init__(self):
        self.office='Delhi'
class state:
    def __init__(self):
        super().__init__()
        self.office='Mumbai'
class District(state,country):
    def __init__(self):
        super().__init__()
        print('Dirstict class')
        self.office='Pune'
d=District()
print(d.__dict__)

# 4th 
# Hybrid Inheritance - mro
class a:
    pass
class b:
    pass
class c:
    pass
class x(a,b,c):
    pass
class y(a,b):
    pass
class s(x,y):
    pass
print(s.mro())


# Encapsulation
# Wrapping up data and methods working on data together in a single unit is called encapsulation.
class finance:
    def __init__(self):
        self.revenue = 2000000    # This public data to make it private do "self.__revenue=10000"
        self.number_sales = 114   # This is public data to make it protected data do "self._number_sales"
f1=finance()
print(f1.__dict__)
class hr :
    def __init__(self):
        self.number_employees=23
        print(f1.revenue)
hr1=hr()
print(f1.__dict__)


# Polymorphism
# Polymorphism is an ability to take many form
emp=['jay','roy','nemo','seema']
company ="Microsoft"
for i in reversed(company):
    print(i)
print("for the list now")
for i in reversed(emp):
    print(i)

# Polymorphism in inheritance
class vec:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price = price
    def get_details(self):
        print("name is:",self.name)
        print("color is:",self.color)
        print("price is:",self.price)
    def max_speed(self):
        print("maximum speed limit is 100")
    def gear(self):
        print("gear change is 6")
class car(vec):
    def max_speed(self):
        print("maximum speed limit is 140")
    def gear(self):
        print("gear change is 7")
v1=vec("Truck",'red',20000000)
c1=car("car",'white',700000)
v1.get_details()
c1.get_details()
v1.max_speed()
c1.max_speed()