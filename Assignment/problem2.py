import math
number=int(input("Enter a number :"))
#positive/negative/zero
if number>0:
    print("number is positive")
elif number<0:
    print("number is negative")    
else:
    print("number is zero")    
    
    
#even/odd

if number%2==0:
    print("Number is Even")   
else:
    print("Number is odd")     
    
    
# dividede by 5 & 7
if number%5==0 and number%7==0:
    print("Divisible by 5 and 7: Yes")    
else:
    print("Divisible by 5 and 7: No")    
    
# Two digit

if 10<=abs(number)<=99:
    print("Two-Digit Number: Yes") 
else:
    print("Two-Digit Number: No")       