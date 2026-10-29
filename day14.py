# Python OOP Advanced

#inheritence

class Student:
    def __init__(self,name,std_id):
        self.name=name
        self.std_id=std_id
           

class myStudents(Student):
    def __init__(self, name, std_id,dept):
        super().__init__(name, std_id)     # super keyword
        self.dept=dept
    def display(self):
        print("Name :",self.name)
        print("Student Id :",self.std_id)
        print("Department name :",self.dept)    
std1 = myStudents("Marjan", 123445,"CSE")

    
std1.display()         





#encasulation



class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
        
    def showBalance(self):
        print("Balance :",self.__balance)     
        
bal=BankAccount(2000)
bal.showBalance()    
print(bal.__balance )   



class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(1000)

account.deposit(500)
account.show_balance()
print(account.__balance) # error, we cann't direct access


#polymorphism

class Dog:
    def display (self):
        print("Dog barking : woaf")
        
class Cat:
    def display(self):
        print("Cat says :meaw!!")        
        
obj1=Dog()
obj2=Cat()
obj1.display()   
obj2.display()     







#abstract method


from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def payment(self,amount):
        pass
class mobileBanking(Payment):
    def payment(self, amount):
        print("Payment :",amount)
    
    
obj=mobileBanking()
obj.payment(3436)   
    
    
        


        
 # challange -1
 
 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show_info(self):
        print("Name :",self.name)
        print("Age :",self.age)    
        
           
class Employee(Person):
    def __init__(self, name, age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def show_info(self):
            print("Name :",self.name)
            print("Age :",self.age) 
            print("Salary :",self.salary)   
obj1=Employee("marjan",23,50000) 
obj1.show_info()       






#challenge--2

class Student:
    def __init__(self,name,std_id):
        self.name=name
        self.std_id=std_id
class CSEStudent(Student):
    def __init__(self,name,std_id,cgpa):
        super().__init__(name,std_id)
        self.cgpa=cgpa
    def display(self): 
        print("Name :",self.name)
        print("Student Id :",self.std_id)
        print("CGPA :",self.cgpa)               
        
obj1=CSEStudent("Ashraf",4324,3.12)        
obj1.display()




#challange -- 3
#ATM BOTH

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self, amount):
        if amount<=0:
            print("Invalid Deposit Amount!!")
        else:
            self.__balance+=amount
            print("Deposit Successful :",amount,"tk.")    
    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient Balance !")        
        elif amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawl Successful :",amount,"tk.")    
        else:
            print("Invalid Amount")    
            
            
    def showBalance(self):
        print("Current Balance :",self.__balance,"tk.")       


object1=BankAccount(5000)            
object1.showBalance()
object1.deposit(1500)
object1.showBalance()
object1.withdraw(700)
object1.showBalance()





#challenge -- 4

class Dog:
    def sound(self):
        print("Dog barking !")
        
class Cat:
    def sound(self):
         print("Cat say : mauw !!")       
         
class Cow:
    def sound(self):
        print("Cow says : hamba hubaa!!!")         


obj1=Dog()
obj2=Cat()
obj3 =Cow()
obj1.sound()
obj2.sound()
obj3.sound()        




#challenge --5

class Employee:
    def show_role(self):
        print("Employee Role : Executive Ofdficer")
        
        
class Manager(Employee):
    def show_role(self):
        print("Manager Role : Team Head ")
        
mnger1=Manager()        
mnger1.show_role()





#challenge --6

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self,length,width):
        pass
       
       
class Rectangle(Shape):
    def area(self, length, width):
        print("Area is :",length*width)
        
        
obj=Rectangle()
obj.area(3,6)
        
        





#home work 


class Student:
    def __init__(self,name,student_id,department):
        self.name=name
        self.student_id=student_id
        self.department=department
    def show_student(self):
        print("Name :",self.name)
        print("Student Id :",self.student_id)
        print("Department :",self.department)    
                
                
class CSEStudent(Student):
    def __init__(self,name,student_id,department,marks):
        
        super().__init__(name,student_id,department)
        self.marks=marks
    def calculate_Total(self):
        return sum(self.marks)                    
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)
    def calculate_grade(self):
        avg=self.calculate_average()
        if avg>=80:
            return "A+"
        elif avg>=70:
            return "A"
        elif avg>=60:
            return "A-"
        elif avg>=50 :
            return "B"
        elif avg>=40:
            return "C"
        else:
            return "F"
        
    def show_result(self):
        
        self.show_student()
        print("Total  Mark :",self.calculate_Total())
        print("Total Average :",self.calculate_average())
        print("Final Grade :",self.calculate_grade())


Student1=CSEStudent("Arosh Khan",124345,"BBA",[65,78,54,76,87])
Student2=CSEStudent("Rhi Akbar",124375,"BBA",[33,78,54,76,87])
Student1.show_result()
Student2.show_result()
            
            