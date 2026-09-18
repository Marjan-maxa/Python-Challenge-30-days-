for number in range(1,6):
    print(number)

   



# i = 1

# while i <= 5:
    
#     print(i)
    
    
    
#  Chaallenge - 1

for j in range(1,21):
    print(j)    
    
    
#  Chaallenge - 2

print("Even Numbers Print")
for ke in range(1,51):
    if ke%2==0:
     print(ke)      
     
     
#  Chaallenge - 3
s=0    
for i in range(1,101):
    s+=i
print("Sum (1-100) is : ",s)      



#  Chaallenge - 4(countdown)

l=5
while(l>=1):
    print(l)
    l-=1
print("Go !")


#  Chaallenge - 5

for m in range(1,21):
    if m%3==0:
        continue
    else:
        print(m)
        



#  Chaallenge - 6

for i in range(1,11):
    if i!=7:
        print(i)
    else:
        break       
    
    

# Mini Project  — guessing game
import random
number=random.randint(1,100)


while True:
    guess=int(input("You guess any one number 1 to 100 :"))
    if guess>number:
        print("Please guess small number")
    elif guess<number:
        print("Please guess larger number")    
    else :
        print("You won the game")
        break    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Mini Project 2 — Multiplication Table    
    
print("===== MULTIPLICATION TABLE =====")    
num=int(input("Enter a number :"))
for n in range(1,11):
        
        print(f"{num}*{n}={ num*n}")        
        
print("===============================")    


    