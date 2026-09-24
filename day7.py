names=("Abir","mash","Raj","Marjan")  # tuple not changable(imortant)
print(names)
print(type(names))

fruits="Apple","Banana","Chery","Watermilon","Apple"
print(fruits)
print(len(fruits))
# fruits[1]="Staberry"  #don't assign because , tuple don't ssupport any item  assignment
print(fruits)
# Students=tuple(("Karim",))  #very  important
# print(Students)
# print(type(Students))

# Employeesa=()
# print(Employeesa)
# print( type(Employeesa))

numbers= (10 ,20,30,40,60)
print(numbers[2:4])
print(numbers[-5:-3])



Schools={"RZS","GGs","Cant","Polish lions","RZS"}
school_list=list(Schools)
print(school_list)
print(type(Schools))
print(len (Schools))

Books=["Bangla","eNGLIS","Math"]
book_set=set(Books  )
print(book_set)
print(type(book_set))






# Challenge 1 — Basic Tuple

numbers=(10,20,30,40,50)
print(numbers)
print(numbers[0])
print(numbers[4])
print(len(numbers))






#Challenge 2 -  Tuple Slicing

num=(10,20,30,40,50,60)
print(num[0:3])
print(num[3:6])
print(num[1:4])





#Challenge 3 — Immutable Test

names=("Marjan","Rahim","Karim")
# names[1]="Hasan"
print(names)  # error because, tuple is immutable, tuple does't support item change






#Challenge 4 — Set & Duplicate

Nums=[10, 20, 10, 30, 20, 40, 30]
Nums_set=set(Nums)
print(Nums_set)


#Challenge 5 — List → Set

fruits=['Apple','Banana','Apple','Mango','Banana']
fruit_set=set(fruits)
print(fruit_set) 





#Challenge 6 — Set → List
marks={10,20 ,30,40 }
mark_set=list(marks)
print(mark_set)





#roadmap_ homework 1

numbers = [10, 20, 10, 30, 20, 40]
numss=set(numbers)
print(numss)



#roadmap_ homework 2


numm_list=list(numss)
print(numm_list)



# Mini project 1

STUDENTS= ['Marjan','Rahim','Karim','Marjan','Sakib','Rahim']
std_set=set(STUDENTS)
print( std_set)



# Mini project 2

userNumbers=list(map(int,input("Enter some Numbers : ").split()))
print( userNumbers)
user_set = set(userNumbers)

print("Unique Set:", user_set)

final_list = list(user_set)

print("Final List:", final_list)



