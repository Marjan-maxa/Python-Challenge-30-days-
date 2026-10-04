number=int(input("Enter a number :"))

if number<2:
    
    print("Not prime number")
    
else:
    for i in range(2,number):
        
        if number%i==0:
            print("Not a prime number")  
            break  
    else:
        print("Prime Numbers")  

print("Prime numbers are:")

for num in range(2, number + 1):

    for i in range(2, num):

        if num % i == 0:
            break

    else:
        print(num)     
        

count=0
for num in range(2, number + 1):

    for i in range(2, num):

        if num % i == 0:
            break

    else:
       count+=1
print("Total Prime numbers are:",count)                 