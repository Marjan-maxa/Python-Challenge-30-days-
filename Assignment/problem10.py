numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    number = int(input("Enter number: "))
    numbers.append(number)


# Sum
total = 0

for number in numbers:
    total = total + number


# Maximum
maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number


# Minimum
minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number


average = total / len(numbers)


# Even and Odd
even = []
odd = []

for number in numbers:

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)


# Duplicate
duplicates = []

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] == numbers[j]:

            if numbers[i] not in duplicates:
                duplicates.append(numbers[i])


ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)


print("\n--- List Result ---")
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Duplicates:", duplicates)
print("Ascending:", ascending)
print("Descending:", descending)