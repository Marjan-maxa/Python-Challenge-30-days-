# topic -- Error Handling (try, except(ValueError,ZeroDivisionError), raise,assert


# try:

        
#     num = int(input("Enter a number: "))
#     print(num)
        
# except ValueError as e:
#     print("Error :",e)
    
# finally:
#     print("Program finished")    
        
        
                    
                    
# try:

#     divisor=23/0
#     print(divisor)
# except ZeroDivisionError:
#     print("Zero can't divide by 23")        
                       
                       


# try:
#     fNum=int(input("Enter first number :"))
#     lNum=int(input("Enter second Number :")) 
#     print(fNum/lNum)
    
# except ValueError:
#     print("Enter valid number")  
# except ZeroDivisionError:
#     print("Zero can't divide by a")
#     print(12);                            
                        
                        
#Challenge 1 — Safe Integer Input
try:

    

        
   num = int(input("Enter a number: "))
   print(num)
        
except :
     print("Invalid Input!")





# Challenge 2 — Division
try:
   num1=int(input("Enter a first number :"))
   num2=int(input("Enter a second number :"))
   print(num1/num2)
except ValueError:
    print("Enter valid Number")   
except ZeroDivisionError:
    print("Cannot divide by zero.")    







#Challenge 3 — List Index

numbers=[10,20,30,40,50]
try:
    print(numbers[3])
except IndexError:
  print("Invalid index.")    



# Challenge 4 — Dictionary Key
student = {
    "name": "Marjan",
    "age": 23
}

try:
    print(student["age"])

except KeyError:
    print("This key does not exist!")




#Challenge 5 — try / except / else / finally



try:
    nums=int(input("Enter a number :"))
    print(nums)
except ValueError as e:
    print("Invalid Input",e)
else:
    print("Successfull Input")    
finally:
    print('Program finished message')    
        
        
#Challenge 6 — Error Message

try:
    number=int(input("Enter a number :"))
    print(number)
    
except ValueError as e:
    print("Error :",e)            







#Challenge 7 — raise

age=int(input("Enter your Age :"))
if age<0:
    raise ValueError("Age can't be negative")
else:
    print("My Age is :",age)
    
    
    


# Challenge 8 — grade calculator


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    else:
        
        raise ValueError("Invalid operator!")

    print("Sum is:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Calculator finished.")    



# Mini project --1-  ATM 


balance=1000;

def show_balance():
    print(" Balance is :",balance)
    
def deposit():
        global balance
        try:
            amount=float(input("Enter deposit Amount :"))  
            if amount<500:
                 raise ValueError("Deposit must be minimum 500 tk.")
             
            balance+=amount
            print("Deposit Successfully !")
        except ValueError as e:
            print("Invalid Input :",e)



def withdrawal():
    global balance
    try:
        
        amount=float(input("Enter withdraw Amount :")) 
        if amount<=499:
            
             raise ValueError("Withdraw amount must be greater than 499 tk.")
        if amount<=balance:
            
            balance-=amount
            print("Withdraw Successfully !")
        else:
            
            print("Insufficient Balance")
    except ValueError as e:
        
        print("Invalid Input :",e)        



while True:
    print("\n--- ATM ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    chiose=input("Enter a choice number :")
    if chiose=="1":
        show_balance()
    elif chiose=="2":
        deposit()
        
    elif chiose=="3":
        withdrawal()
    elif chiose=="4":
        print("Thank you sir")    
    else:
        print("Choice Invalid !")            








#mini project --2-  number analyzer

try:
    num=int(input("Enter a number :"))
    if num%2==0:
        print(num ,"is even")
    else:
        print(num, "is odd")    
        
        #positive /negative
    if num<0:
        print(num,"is negative")   
    elif num>0:
        print("is positive")
    else:
        print(num, "is zero") 
    
    #square
    square=num*num
    print("Square is :",square)
except ValueError:
    print("Invalid number !")    
finally:
    print("Programm finished !")    
        
        