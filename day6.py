#list topic in python 

fruits=["Apple,","Banana,","Carry"]
print(fruits)
print(type(fruits))

mixed = [10, "Hello", 3.5, True]
print(mixed)
print(type(mixed[2]))
mixed[-1]=75

thislist = set(("apple", "banana", "cherry"))
print(thislist)
print(type(thislist))

names={"Marjan","Raj","Hamim"}
print(names)
names.discard("Raj")
names.add("Mash")
print(names)

thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)
print(len(thislist))




numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])    
print(numbers[::-1])    # reverse
print("maximam :",max(numbers))

print("minimum :",min(numbers))



#challange 1

Numbers=[10, 20, 30, 40, 50]
print(Numbers)
print(Numbers[0])
print(Numbers[4])




#challange 2
names=["Marjan","Rahim","Karim","Sakib"]
names[1]="Hasan"
print(names)


#challenge 3

fruits=["Apple","Banana","Mango"]
fruits.append("Orange")
fruits.append("Guava")
print(fruits)



#challenge 4
numbers=[10,20,30,40,50]
numbers.remove(30)
numbers.remove(50)
print(numbers)

#challenge 5
numbers=[10,20,30,40,50,60]
print(numbers[0:3])
print(numbers[3:6])
print(numbers[1:4])



#challenge 6
numbers = [45, 12, 89, 34, 67, 5]
print(max(numbers))
print(min(numbers))



# mini project 1
marks = [75, 82, 68, 90, 85]
print("All Marks :",marks)
print("Highest Marks :",max(marks))
print("Lowest Marks :",min(marks))
print("Total Subjects :",len(marks))




#mini project-2
shopping = ["Rice", "Oil", "Eggs"]
shopping.append("Milks")

shopping.remove("Eggs")

shopping.append("Chicken")
print("Final Shopping List: ",shopping)

print("Total Items: ",len(shopping))



#  H.W (home work)
userNumber=list(map(int,input("Enter five numbers :").split()))
print(userNumber)
print(max(userNumber))
print(min(userNumber))


