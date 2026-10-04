def add_student():

    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    cgpa = float(input("Enter CGPA: "))

    with open("students.txt", "a") as file:

        file.write(student_id + "," + name + "," +
                   department + "," + str(cgpa) + "\n")

    print("Student added successfully!")


def display_students():

    try:

        with open("students.txt", "r") as file:

            data = file.readlines()

            if len(data) == 0:
                print("No student found")

            else:

                for line in data:

                    student = line.strip().split(",")

                    print("\nID:", student[0])
                    print("Name:", student[1])
                    print("Department:", student[2])
                    print("CGPA:", student[3])

    except FileNotFoundError:

        print("File not found")


def search_student():

    student_id = input("Enter student ID: ")

    try:

        with open("students.txt", "r") as file:

            found = False

            for line in file:

                student = line.strip().split(",")

                if student[0] == student_id:

                    print("ID:", student[0])
                    print("Name:", student[1])
                    print("Department:", student[2])
                    print("CGPA:", student[3])

                    found = True

            if found == False:
                print("Student not found")

    except FileNotFoundError:

        print("File not found")


def calculate_result():

    try:

        with open("students.txt", "r") as file:

            total_cgpa = 0
            count = 0
            highest = 0

            for line in file:

                student = line.strip().split(",")

                cgpa = float(student[3])

                total_cgpa = total_cgpa + cgpa
                count = count + 1

                if cgpa > highest:
                    highest = cgpa

            if count > 0:

                print("Total CGPA:", total_cgpa)
                print("Average CGPA:", total_cgpa / count)
                print("Highest CGPA:", highest)

            else:
                print("No student found")

    except FileNotFoundError:

        print("File not found")


while True:

    print("\n--- Student Result Management ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Calculate Result")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_result()

    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Invalid choice")