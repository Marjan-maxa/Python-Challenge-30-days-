# Name validation

while True:

    try:

        name = input("Enter your name: ")

        if name == "":
            raise ValueError("Name cannot be empty")

        break

    except ValueError as error:

        print("Error:", error)


# Age validation

while True:

    try:

        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError("Age cannot be negative")

        break

    except ValueError:
        print("Please enter a valid age")


# Marks validation

while True:

    try:

        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        break

    except ValueError as error:

        print("Error:", error)


# CGPA validation

while True:

    try:

        cgpa = float(input("Enter CGPA: "))

        if cgpa < 0 or cgpa > 4:
            raise ValueError("CGPA must be between 0 and 4")

        break

    except ValueError as error:

        print("Error:", error)


# Division

while True:

    try:

        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        result = number1 / number2

        print("Division:", result)

        break

    except ZeroDivisionError:

        print("Cannot divide by zero")

    except ValueError:

        print("Please enter valid numbers")


print("\n--- Student Information ---")
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("CGPA:", cgpa)