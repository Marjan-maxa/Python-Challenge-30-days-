try:
    students={}
    while True:
        

        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display Students")
        print("4. Update CGPA")
        print("5. Delete Student")
        print("6. Exit")
        choice=input("Enter your choice :")
        
        
        if choice=="1":
            student_id=input("Enter student Id :")
            name=input("Enter Student Name :")
            department_Name=input("Enter departmenot name :")
            cgpa=input("Enter cgpa :")
            
            students[student_id]={
                "name":name,
                "department":department_Name,
                "cgpa":cgpa
            }
            print("Student Added Successfully!")
        elif choice=="2":   
            student_id=input("Enter id :")
            if student_id in students:
                print("Name:", students[student_id]["name"])
                print("Name:", students[student_id]["name"])
                print("Department:", students[student_id]["department"])
                print("CGPA:", students[student_id]["cgpa"])
            else:
                print("Student not found!")    
                
        elif choice=="3":
                  
            if len(students) == 0:
                print("No student found")

            else:
                for student_id in students:

                    print("\nID:", student_id)
                    print("Name:", students[student_id]["name"])
                    print("Department :",students[student_id]["department"])
                    print("CGPA:", students[student_id]["cgpa"])
                    
        elif choice=="4":
            student_id=input("Enter id :")
            if student_id in students:
                cgpa=input("Enter new cgpa : ")
                students[student_id]["cgpa"]=cgpa
                
                print("CGPA Updated")                
            else:
                print("Student not found")    
            
        elif choice=="5":
                 student_id=input("Enter id :")
                 if student_id in students:
                     del students[student_id]
                     print("Deleted Successfully!")
                 else:
                     print("Student not found!")    
                     
        elif choice=="6":
            print("Thanks take our service")     
            break
        
        else:
            print("Invalid choice, Please try again")        
            
except ValueError:
    print("System a bug error!!!!! ")            