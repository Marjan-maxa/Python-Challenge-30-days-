
# challange --1 
from  math import *
num=int(input("Enter a number :"))
print("Square root :",round(sqrt(num),2))
print("Square :",pow(num,2))
print("Factorial is :",factorial(num))


# challange --2

import random
ranNumber=random.randint(1,100)
print("Random number is :",ranNumber)


#challange --3
import random
names = ["Marjan", "Hasan", "Rahim", "Karim"]
print("Selected Student :",random.choice(names))


#challange --4


#calculator.py:

def sumation(x, y):
    return x+y;
def  mul(x,y):
    return x*y

def substraction(x,y):
    return x-y

def div(x,y):
    return x/y


# day12.py :
import calculator
print(calculator.sumation(1,2))
print(calculator.substraction(10,5))
print(calculator.mul(2, 8))
print(calculator.div(9,2))



#challange 5--
from math import sqrt,pi
print("Square root :",sqrt(8))
print("Tne value of pi :",round(pi,4))


#challange --6 

import random as r
print("Generated Random number :",r.randint(1,50))







#Day 12 Homework — Password Generator
import random
length=int(input("Enter password length :"))

letters = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"
chars=letters+uppercase+numbers+symbols
password=""

for i in range(length):
    password+=random.choice(chars)
print("Generated password is :",password)    
















# Mini Project 1 — Random Student Picker

import random
students=[]

try:
    
    def add():
        studentName=input("Enter your student name :")
        students.append(studentName)
        print("Student Added successfully !")
    
    def showStudent():
        if len(students)==0:
            print("Empty students")
        else:
            print("Students are :\n")
            for stu in students:
                print(stu)    
    
    def pickStu():
         if len(students)==0:
             print("Empty students")
         else:
             selected=random.choice(students) 
         print("Selected Strudent :",selected)       
    
    def exitSys():
        print("Thanks for our Services,Give your feedback !")
        
    
    while True:
        
        print("--- Student Picker ---\n")
        print("1. Add Student\n")
        print("2. Show Students\n")
        print("3. Pick Random Student\n")
        print("4. Exit")
        chiose=int(input("Enter your chiose number :"))
        
        if chiose==1:
            add()
        elif chiose==2:
            showStudent()
        elif chiose==3:
            pickStu()
            
        elif chiose==4:
           exitSys()
           break
        else:
            print("Invalid Input ,Please try Again") 
            
except ValueError:
    print("System crushed!!!")
    
    
    
    
#  mini project -- 2
    
try:
    def add(x,y):
        sum=x+y
        print("Suimation is:",sum)
    
    
    def Substract(x,y):
        sub=x-y
        print("Substraction is :",sub)
    def Multiply(x,y):
        mul=x*y
        print("Multiplication is :",mul)        
    
    def Divide(x,y):
        div=x/y
        print("Divition is :",div)   
        
    def Exit():
        print("Thanks for our Services,Give your feedback !")     
        
    while True:
         print("--- Simple Calculator --~-\n")
         print("1. Add\n")
         print("2. Subtraction\n")
         print("3. Multiply\n")
         print("4. Divition\n")
         print("5. Exit")
         chiose=int(input("Enter your chiose number :"))
         if chiose==5:
             Exit()
             break
         elif chiose not in [1, 2, 3, 4]:
             
             print("Invalid Input, Please try Again")
             break
             
             
         x=int(input("Enter your first number :"))
         y=int(input("Enter your second number :")) 
         
         if chiose==1:
             add(x,y)
         elif chiose==2:
             Substract(x,y)
             
         elif chiose==3:
             Multiply(x,y) 
         elif chiose==4:
             Divide(x,y)
         
         else:
             print("Invalid Input,Please try Again")      
             
except ValueError:
    print("System are crashed for rules breking!!!!!")
                               
                               
                               
                            