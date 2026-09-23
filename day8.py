# day 8  -- dictionaries
#Crud Operations
# students={
#     "name":"Marjan",
#     "Roll":50,
#     "batch":"D-93",
#     "Department":"CSE"
# }

# print(students)
# print(type(students))
# print(students["name"])
# print(students.keys())
# print(students.values())
# print(students.items())
# students["cgpa"]=3.74
# students["Address"]="Rangpur,Bangladesh"
# print(students)
# students ["cgpa"]=3.80
# print(students)
# students.pop("Address")
# print(students)
# del students['Roll']
# print(students)


 #challenge --1
 
# students={
#         "Name":"Marjan",
#         "Age":23,
#         "Department":"CSE",
#         "cgpa":3.75
#  }
# print(students)

#  #challenge --2
 
# print(students["Name"])
# print(students["Age"])
# print(students["cgpa"])


#  #challenge --3
 
# student={
#     "name":"Marjan",
#     "age":23,
#     "cgpa":3.50 ,
# }
# print(student)
# student["age"]=24
# student["cgpa"]=3.75
# print(student)  


#Challenge 4 — Add Data
# student = {
#     "name": "Marjan",
#     "age": 23
# }
# student["department"]="CSE"
# student["semester"]="6th"
# print(student)


# Challenge 5 — Delete

# student = {

#     "name": "Marjan",
#     "age": 23,
#     "department": "CSE",
#     "cgpa": 3.75
# }

# student.pop("age")
# student.pop("cgpa")
# print(student)

# Challenge 6 — Keys & Values

# student = {
#     "name": "Marjan",
#     "age": 23,
#     "department": "CSE"
# }
# print(student.keys())
# print(student.values())


#Roadmap Homework — Student Record System

#step 1
# student={
#     "name":"Raj",
#     "id":101,
#     "deartmpent":"EEE",
#     "CGPA":"3.76",
#     "Address":"Rangur,Bangladesh" ,
#     "E-mail Adress":"praj12@gmail.com"   
# }

# #step 2
# print(student)
# #step 3
# student["CGPA"]=3.85
# #step 4
# student["semester"]="6th"
# # step 5
# student.pop("Address")
# print(student)



#mini project -1

student={
    "name":"Raj",
    "Age":23,
    "id":101,
    "deartmpent":"EEE",
    "semester":"7th",
    "CGPA":"3.76",
    
    "EmailAdress":"praj12@gmail.com"   
}   
print(student["name"])
print(student["deartmpent"])
print(student["CGPA"])
student["semester"]="8th"
student["Address"]="Rangpur"
student.pop("EmailAdress")
print(student)

#Mini Project 2 — Simple Contact

contact = {
    "name": "Raj",
    "phone": "01700000000",
    "email": "raJK@gmail.com",
    "city": "Rangpur"
}   
print(contact["name"])
contact["phone"]="01954233387"
contact.pop("city")
print(contact)