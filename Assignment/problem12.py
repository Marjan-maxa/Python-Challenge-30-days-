def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def find_max(numbers):

    maximum = numbers[0]

    for number in numbers:

        if number > maximum:
            maximum = number

    return maximum


def find_min(numbers):

    minimum = numbers[0]

    for number in numbers:

        if number < minimum:
            minimum = number

    return minimum


def calculate_average(numbers):

    total = 0

    for number in numbers:
        total = total + number

    return total / len(numbers)


def is_prime(number):

    if number < 2:
        return False

    count = 0

    for i in range(1, number + 1):

        if number % i == 0:
            count = count + 1

    if count == 2:
        return True
    else:
        return False


try:

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))

    numbers = []

    n = int(input("\nHow many numbers? "))

    for i in range(n):
        number = int(input("Enter number: "))
        numbers.append(number)

    print("Maximum:", find_max(numbers))
    print("Minimum:", find_min(numbers))
    print("Average:", calculate_average(numbers))

    check = int(input("\nEnter a number to check prime: "))

    if is_prime(check):
        print("Prime Number")
    else:
        print("Not Prime")

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")