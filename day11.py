file=open("student.txt","r")

data=file.read()
data=file.read() # eta exact no. of character print kora
line=file.readline()
print(data)
print(line)
print(file.readline())
print(file.readline())
print(data)
lines=file.readlines()
print(lines)
print(type(lines))

for val in file:

    print(val)
    

file=open("student.txt","a")

file.write("hello world !\n")
file.write("Hey Mahirrum\n")
file.close()


with open("student.txt", "w") as file:
    file.writelines([
        "marjan\n", "CSE\n", "python"
    ])

file = open("student.txt", "r")
print(file.read())
file.close()




create new file ,write ,read
myFile=open("marjan.txt","x")
myFile.write("boss kemon Aso")
myFile.close()


with open () - it can automatically close the file

with open("student.txt","w+") as ourFile:
    ourFile.write("Name : Marjan\n")
    ourFile.write("Department : CSE")
    ourFile.seek(0)  
    d=ourFile.read()
print(d)    
    

file not found

with open("demo.txt","r") as topFile:
    print(topFile.read())    


file handle wi8th error handle

try:
    with open("fgdf.txt","r") as we:
        print(we.read())
except:
    print("File not found")        

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("student.txt","w") as val:
    val.write("10\n")
    val.write("20\n")
    val.write("30\n")
    val.write("40")
    

with open("student.txt", "r") as file:
    data = file.read()

print(data)


with open("student.txt", "r") as Dfile:
    numbers = []

    for line in Dfile:
        numbers.append(float(line.strip()))

print(numbers)
print(type(numbers))



with open("student.txt", "r") as file:
    print(file.tell())
    
    
with open("student.txt", "r") as file:
    print(file.read(5))

    file.seek(0)

    print(file.read(5))    










# challenge 1-- create and write

with open("student.txt","x") as file:
    file.write("Name : Marjan\n")
    file.write("Department : CSE\n")
    file.write("Semester : 7th")
    
    
    
#challenge 2 -- Read file

with open("student.txt","r") as demofile:
    data=demofile.read()
print(data)        








#Challenge 3 — Append

with open("student.txt","a") as file:
    file.write("\nCGPA :3.75")
    
    











#challenge 4 -- read line by line

with open("student.txt","r") as LIST:
    for val in  LIST:
        print(val.strip())





# Challenge 5 — Numbers File           

with open("number.txt","w") as value:
    
    value.write("10\n")
    value.write("20\n")
    value.write("30\n")
    value.write("40\n")
    value.write("50\n")
    
    
    


#    Challenge 6 — File Not Found

try:
    with open("fghrty.txt","r") as file:
        file.read()
except:
    print("File not found.")        
    
    
    



# Challenge 7 — Copy Content

with open("source.txt","r") as source:
    data=source.read()   
    
print(data) 

with open("backup.txt","w") as backup:  
    D=backup.write(data)



# Challenge 8 — File Pointer


with open("demo.txt","r") as demo:
    Data=demo.read(6)    
print(Data)    

with open("demo.txt","r") as demo:
    print(demo.tell())
    print(demo.seek(0))
    print(demo.read(6))
    
    



# HOME WORK


with open("number.txt","w") as value:
    
    value.write("10\n")
    value.write("20\n")
    value.write("30\n")
    value.write("40\n")
    value.write("50\n")    
    
with open("number.txt","r") as files:
    lines = files.readlines()

numbers = []
for line in lines:
    numbers.append(int(line.strip()))
    
total=sum(numbers)
average=total/len(numbers)
maximum=max(numbers)
minimum=min(numbers) 
print("Total :",total)
print("Average :",average)  
print("Maximum :",maximum)  
print("Minimum :",minimum)       



# mini  roject --1 -Student File System

try:
    data=input("Enter your information :\n")
    with open("student.txt","w") as fil:
        fil.write(data)
    with open("student.txt","r") as fil:  
          
        result=fil.read()   
    print(result)
except:
    print("Something went worng")






#mini project 2-- Simple Notes App


try:
    
    def Add_notes():
        notes=input("Enter your notes :")
        with open("notes_app.txt","a") as file:
            file.write(notes+" \n")
        print("Add note Successfully!")    
            
    def View_notes():
        with open("notes_app.txt","r") as file:
            data=file.read()
            
        print("Your notes :",data)
    def Exit():
        print("Thanks,Enjoyed our Service !")  
    
    
    
    while True:
        
        print("\n--- Note App ---")
        print("1. Add Notes")
        print("2. View Notes")
        print("3. Exit")
              
        chiose=input("Enter yur choice number :")
        if chiose=="1":
            Add_notes()
        elif chiose=="2":
            View_notes()
        elif chiose=="3":
            Exit()
            break
        else:
            print("Invalid number,please try again!")            
                  
except:
    print("Something went worng")              
              
        
                        