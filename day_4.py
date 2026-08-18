age=20;

    
    
print(age!=20) 
print(age>18)   


marks=int(input("Enter your Number :"));
if marks>=80:
    print("A+")
elif marks>=75:
    print("A")
elif marks>=70:
    print("B+")  
elif marks>=65:
    print("B")      
else:
    print("Fail")        
    
Age=25;
if Age>=18 & Age<=30:
    print("Valid Age")    
    
day=(input("Enter Anyone name of days :"))
if day=="Friday" or day=="Saterday" :
    print("WeekEnd") 
else:
    print("Invalid")      
    
 
#basic Login System 🔐
userName=input("Enter your Username :") 
password=int(input("Enter your Password :"))
if(userName=="Admin" and password==1234) :
    print("Loggedin Successfull!")
else:
    print("Invalid Password and UserName")    
    



# DAY 4 SUBMISSION

# Challenge -- 1

numbers=int(input("Enter a number :"))
if numbers>0:
    print(f"{numbers} is positive")
elif numbers<0:
    print(f"{numbers} is negative")   
    
else:
    print(f"{numbers} is zero")     


 
 
 
    
# Challenge -- 2 (ever or odd by user)

num=int(input("Enter a number :"))
if num%2==0:
    print(f"{num} is even") 
else:
    print(f"{num} is odd")       


#Challenge -- 3


marks=int(input("Enter your Number :"));
if marks>=80:
    print("A+")
elif marks>=70:
    print("A")
elif marks>=60:
    print("B")  
elif marks>=50:
    print("C")   
elif marks>=40:
    print("B")   
else:
    print("Fail")        
    



#Challenge -- 4(Login System 🔐)

userName=input("Enter your Username :") 
password=int(input("Enter your Password :"))
if(userName=="admin" and password==1234) :
    print("Loggedin Successfull!")
    
elif (userName!="admin" and password==1234):
    print("User not Found!")
elif (userName=="admin" and password!=1234):
    print("Wrong Password")       
else:
    print("Invalid Password and UserName")    
 
 
 
 
 
 
 
 
 # Challenge --5   
num1=int(input("Enter a first number :")) 
num2=int(input("Enter a Second number :")) 
num3=int(input("Enter a Third number :")) 

if (num1>num2 and num1>num3 ):
    print(f"{num1} is Largest number")
    
elif(num2>num3 and num2>num1):
    print(f"{num2} is Largest number")   
    
else:
    print(f"{num3} is Largest number")     
    
    
    
    
# Mini Project -- 1
print("===== LOGIN SYSTEM =====")
userName=input("Enter your Username     :") 
password=int(input("Enter your Password :"))
if(userName=="Admin" and password==1234) :
    print("Loggedin Successfull!\nWelcome Admin.")
else:
    print("Invalid  UserName and Password ")    






# Mini Project -- 2
print("===== STUDENT RESULT =====")
name=input("Enter your Name :")
marks=int(input("Enter your Number :"));
if marks>=80:
    print("A+ → Excellent!")
elif marks>=70:
    print("A → Very Good!")
elif marks>=60:
    print("B → Good!")  
elif marks>=50:
    print("C → Average")   
elif marks>=40:
    print("D → Need Improvement")   
else:
    print("Fail → Better luck next time!")
    
print("==========================")    
    