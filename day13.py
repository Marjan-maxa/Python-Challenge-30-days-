class Student:

    pass
st1=Student()
st1.name="Raj"
st1.department="CSE"
st1.cgpa=3.73
print(f"\n{st1.name}\n{st1.department}\n{st1.cgpa}")

class Student:
    def __init__(self,name,dept,cgpa,roll):
        pass
        
        self.name=name
        self.dept=dept
        self.cgpa=cgpa
        self.roll=roll
student1=Student("marjan","CSE",3.73,5)    
student2=Student("Mahidul","EEE",3.52,11)    
print(f"\n{student1.name} \n{student1.dept} \n{student1.cgpa} \n{student1.roll}")
print(f"\n{student2.name} \n{student2.dept} \n{student1.cgpa} \n{student2.roll}")        


class Student:
    def __init__(self,name,Address):
        self.name=name
        self.Address=Address
    
    def display(self):
        print("Name :",self.name)
        print("Address :",self.Address)    
    def update_value(self,name):
        self.name=name
std1=Student("Sifat","Salbon,Mistripara")
std1.display()    
std1.Address="Nurpur Alamnagar,Rangpur"   #  value update

std1.display()

std1.update_value("Iron Man ")  # update valu with method
print("After 2nd time Update :")
std1.display()



class markSheet:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def cal_total(self):
        total=self.mark1+self.mark2+self.mark3    
        return total
    def average(self):
        total=self.cal_total()
        avg=total/3
        return avg  
    
st1=markSheet("Alfaz",76,87,91)    
print("Student name :",st1.name)
print("Total marks :",st1.cal_total())  
print("Average mark :",round(st1.average(),2)) 









#challenge --1


class Student:
    pass
student1=Student()
student1.name="Marjan"
student1.student_id=125226
student1.department="CSE"
student1.cgpa=3.73
print(f"\n{student1.name}\n{student1.student_id}\n{student1.department}\n{student1.cgpa}")







#challenge --2

class Student:
    def __init__(self,name,id,department,cgpa):
        self.name=name
        self.id =id
        self.department=department
        self.cgpa=cgpa
    def show_students(self):
        print("Name :",self.name) 
        print("Id :",self.id)
        print("Department :",self.department)
        print("CGPA :",self.cgpa)   
     
std=Student("Mahtina",1234,"Civil",3.34)
std.show_students()        











# challenge --3


class Student:
    def __init__(self,name,id,department,cgpa):
        self.name=name
        self.id =id
        self.department=department
        self.cgpa=cgpa
    def show_students(self):
        print("Name :",self.name) 
        print("Id :",self.id)
        print("Department :",self.department)
        print("CGPA :",self.cgpa)   
     
student1=Student("Mahtina",1234,"Civil",3.34)
student2=Student("Mahin",3264,"CSE",3.74)
student3=Student("Rahi Akbar",8974,"Civil",3.54)
student1.show_students() 
student2.show_students()
student3.show_students()









# challenge --4 (cgpa update)


class Student:
    def __init__(self,name,id,department,cgpa):
        self.name=name
        self.id =id
        self.department=department
        self.cgpa=cgpa
    def show_students(self):
        print("Name :",self.name) 
        print("Id :",self.id)
        print("Department :",self.department)
        print("CGPA :",self.cgpa)   
     
student1=Student("Mahtina",1234,"Civil",3.34)
student2=Student("Mahin",3264,"CSE",3.74)
student3=Student("Rahi Akbar",8974,"Civil",3.54)
student1.cgpa=3.44

student1.show_students() 
student2.cgpa=3.79
student2.show_students()
student3.cgpa=3.69
student3.show_students()









#challenge --5 (marks)


class Student:
    def __init__(self,mark1,mark2,mark3,mark4,mark5):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.mark4=mark4
        self.mark5=mark5
    def total_mark(self):
        total=self.mark1+self.mark2+self.mark3+self.mark4+self.mark5    
        return total
    
    def avg_mark(self):
        total=self.total_mark()
        avg=total/5
        return avg
    
    def highest_mark(self):
        Highest=max(self.mark1,self.mark2,self.mark3,self.mark4,self.mark5)
        return Highest  
    
    def lowest_mark(self):
            Lowest=min(self.mark1,self.mark2,self.mark3,self.mark4,self.mark5)
            return Lowest
        
        
std=Student(65,87,43,87,94)        

print("Total mark :",std.total_mark())
print("Average mark :",std.avg_mark())
print("Highest mark :",std.highest_mark())
print("Lowest mark :",std.lowest_mark(
    
))







#  home work


class Student:
    def __init__(self):
         self.name=input("Enter your name :")
         self.student_id=input("Enter your Id :")
         self.department=input("Enter your Department :")
         self.marks=[]
         for j in range(5):
             mark=float(input((f"Enter your mark{j+1} :")))
             self.marks.append(mark)
             
             
    def show_std(self):
        print("Name :",self.name)         
        print("Student Id :",self.student_id)
        print("Department :",self.department)
    
    def calculate_mark(self):
            total=sum(self.marks)
            print("Total mark :",total)
    
    def calculate_avg(self):
        average=sum(self.marks)/len(self.marks)
        print("Average marks ",average)
        
    def calculate_grade(self):
        avg=sum(self.marks)/len(self.marks)
        if avg>=80:
            grade="A+"
        elif avg>=70:
            grade="A"
        elif avg>=60:
            grade="B"
        elif avg>=50:
            grade="C"
        elif avg>=40:
            grade="D"
        else:
            grade="F"   
        print("Your Grade :",grade)        
        
std1=Student()    
std1.show_std()
std1.calculate_mark()
std1.calculate_avg()
std1.calculate_grade()                     