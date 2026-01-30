# class Student:
#     roll_number =8

#     def __init__(self,roll_number):
#      self.roll_number = roll_number

#     def learn(self):
#      print = ("learning...")

# pawan = Student("150")
# print(pawan.roll_number)
# print(pawan.learn())

# print(Student.roll_number)


# class worker:
#   pass

# somya = worker()
# somya.skills = ["tp acha karta hai", "bol bachan"]

# def teach():
#  return somya.skills

# print(somya.teach())


# aayush = worker()
# #print(aayush.skills)

# worker.skills ("READ")
# print(aayush.skills)


# Facalty.skills = ["read"]
# print(gatik.skills)

# class Person:
#     def_init_(self,fname,lname):
#       self.fname=fname
#       self.lname=lname

#     def print_full_name(self):
#        return self.fname+self.lname
    

# class User(Person):
#    pass

# user_one=User("John","Cena")
# print(user_one.fname)
# print(Person_one.lname)

# user_one=User("John","Cena")
# print(user_one.fname)
# print(user_one.lname)


# user_input("Enter your username:")
# user_password("Ener your password:")

# class user:

#  def __init__(self ,username,password):
#    self.username = username
#    self.userpassword = password

#    def get_password(self):
#      return self.__password
   

# class Auth(user):
#   def __init__(self,username, password):
#     super(),__init__(username,password)

#     def login(self,username. password):
#       if username == user_input and self.get_password() == user_password:
#         return True:
#       else:
#         return False
#     def reg()
#       pass 


#     obj = Auth('prasad','123')
#     print(obj), login(user_input, user_password)



# from abc import ABC, abstractmethod 

# class Human(ABC):

#     @abstractmethod
#     def talk(self):
#         print("talking..")
#         pass

# class Man(Human):
#     def talk(self):
#         print("hmmmm")

# person = Man()


'''Create a class Car with attributes brand and model. Create 3 car objects and print their details.'''

# class car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
# c1 = car("Audi","XM")
# c2 = car("BMW","M5")
# c3 = car("Tata","safari")

# print(c1.brand,c1.model)
# print(c2.brand,c2.model)
# print(c3.brand,c3.model)


'''Create a class Student with attributes name, age, and marks. Add a method that prints “Pass” if marks > 40 else “Fail”.'''

# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
    
#     def check_result(self):
#         if self.marks>40:
#             print("Pass")
#         else:
#             print("Fail")
# s = Student("Pawan","23",56)
# s.check_result()


'''Create a class Rectangle with methods to compute area and perimeter.'''

# class Rectangle:
#     def __init__(self,w,h):
#         self.w=w
#         self.h=h

#     def area(self):
#         return (self.w * self.h)
    
#     def parimeter(self):
#         return 2*(self.w + self.h)
    
# s = Rectangle(4,5)
# print(s.area(),s.parimeter())


'''Create a class BankAccount with:
deposit()
withdraw()
check_balance()'''

# class BankAccount:
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance

#     def deposit(self,amt):
#         self.balance+=amt
    
#     def withdraw(self,amt):
#         if amt<=self.balance:
#             self.balance-=amt
#         else:
#             print("Insaficient balance")
        
#     def check(self):
#         print("Balance =",self.balance)

# s = BankAccount("Pawan",400)
# s.deposit(500)
# s.withdraw(200)
# s.check()


'''Create a class Calculator with methods add, subtract, multiply, divide.'''

# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a - b
#     def mul(self,a,b):
#         return(self,a*b)
#     def div(self,a,b):
#         return a/b
# s = Calculator()
# print(s.sub(9,9))


'''Create a class Laptop with attributes brand, price. Add a method to show details.'''

class Laptop:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def show(self):
        print(self.brand,self.price)

s = Laptop("Apple",75000)
s.show()