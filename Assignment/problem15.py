students = {}


def add_student():

    try:

        student_id = input("Enter Student ID: ")

        if student_id in students:
            print("Student ID already exists!")
            return

        name = input("Enter Name: ")
        department = input("Enter Department: ")

        marks = []

        for i in range(1, 6):

            mark = float(input("Enter Mark " + str(i) + ": "))

            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100")
                return

            marks.append(mark)

        total = sum(marks)
        average = total / 5

        if average >= 80:
            grade = "A+"

        elif average >= 70:
            grade = "A"

        elif average >= 60:
            grade = "A"

        elif average >= 50:
            grade = "B"

        elif average >= 40:
            grade = "C"

        elif average >= 33:
            grade = "D"

        else:
            grade = "F"

        students[student_id] = {
            "name": name,
            "department": department,
            "marks": marks,
            "total": total,
            "average": average,
            "grade": grade
        }

        print("Student added successfully!")

    except ValueError:

        print("Please enter valid marks")


def view_students():

    if len(students) == 0:

        print("No student found")

    else:

        for student_id in students:

            student = students[student_id]

            print("\n--------------------")
            print("ID:", student_id)
            print("Name:", student["name"])
            print("Department:", student["department"])
            print("Marks:", student["marks"])
            print("Total:", student["total"])
            print("Average:", student["average"])
            print("Grade:", student["grade"])


def search_student():

    student_id = input("Enter Student ID: ")

    if student_id in students:

        student = students[student_id]

        print("\nID:", student_id)
        print("Name:", student["name"])
        print("Department:", student["department"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Average:", student["average"])
        print("Grade:", student["grade"])

    else:

        print("Student not found")


def calculate_result():

    student_id = input("Enter Student ID: ")

    if student_id in students:

        student = students[student_id]

        total = sum(student["marks"])
        average = total / 5

        student["total"] = total
        student["average"] = average

        if average >= 80:
            student["grade"] = "A+"

        elif average >= 70:
            student["grade"] = "A"

        elif average >= 60:
            student["grade"] = "A"

        elif average >= 50:
            student["grade"] = "B"

        elif average >= 40:
            student["grade"] = "C"

        elif average >= 33:
            student["grade"] = "D"

        else:
            student["grade"] = "F"

        print("Result calculated successfully!")

        print("Total:", student["total"])
        print("Average:", student["average"])
        print("Grade:", student["grade"])

    else:

        print("Student not found")


def update_student():

    student_id = input("Enter Student ID: ")

    if student_id in students:

        print("1. Update Name")
        print("2. Update Department")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Enter new name: ")

            students[student_id]["name"] = name

            print("Name updated")

        elif choice == "2":

            department = input("Enter new department: ")

            students[student_id]["department"] = department

            print("Department updated")

        else:

            print("Invalid choice")

    else:

        print("Student not found")


def delete_student():

    student_id = input("Enter Student ID: ")

    if student_id in students:

        del students[student_id]

        print("Student deleted successfully!")

    else:

        print("Student not found")


def class_statistics():

    if len(students) == 0:

        print("No student found")
        return

    total_average = 0
    highest_average = 0
    lowest_average = 100

    highest_student = ""
    lowest_student = ""

    pass_count = 0
    fail_count = 0

    for student_id in students:

        student = students[student_id]

        average = student["average"]

        total_average = total_average + average

        if average > highest_average:

            highest_average = average
            highest_student = student["name"]

        if average < lowest_average:

            lowest_average = average
            lowest_student = student["name"]

        if student["grade"] == "F":
            fail_count = fail_count + 1
        else:
            pass_count = pass_count + 1

    class_average = total_average / len(students)

    print("\n--- Class Statistics ---")
    print("Class Average:", class_average)
    print("Highest Average:", highest_average)
    print("Highest Student:", highest_student)
    print("Lowest Average:", lowest_average)
    print("Lowest Student:", lowest_student)
    print("Passed Students:", pass_count)
    print("Failed Students:", fail_count)


def save_students():

    with open("students_result.txt", "w") as file:

        for student_id in students:

            student = students[student_id]

            file.write(student_id + "|")
            file.write(student["name"] + "|")
            file.write(student["department"] + "|")

            for mark in student["marks"]:
                file.write(str(mark) + ",")

            file.write("|")
            file.write(str(student["total"]) + "|")
            file.write(str(student["average"]) + "|")
            file.write(student["grade"] + "\n")

    print("Data saved successfully!")


def load_students():

    try:

        with open("students_result.txt", "r") as file:

            for line in file:

                data = line.strip().split("|")

                if len(data) >= 7:

                    student_id = data[0]
                    name = data[1]
                    department = data[2]

                    marks_data = data[3].split(",")

                    marks = []

                    for mark in marks_data:

                        if mark != "":
                            marks.append(float(mark))

                    total = float(data[4])
                    average = float(data[5])
                    grade = data[6]

                    students[student_id] = {
                        "name": name,
                        "department": department,
                        "marks": marks,
                        "total": total,
                        "average": average,
                        "grade": grade
                    }

        print("Data loaded successfully!")

    except FileNotFoundError:

        print("No saved data found.")


# Load previous data
load_students()


# Main Menu

while True:

    print("\n================================")
    print(" Student Result Management")
    print("================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Result")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Class Statistics")
    print("8. Save Data")
    print("9. Load Data")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        calculate_result()

    elif choice == "5":

        update_student()

    elif choice == "6":

        delete_student()

    elif choice == "7":

        class_statistics()

    elif choice == "8":

        save_students()

    elif choice == "9":

        load_students()

    elif choice == "10":

        print("Thank you!")
        break

    else:

        print("Invalid choice!")