N = int(input("Enter a number: "))

sum_all = 0
sum_even = 0
sum_odd = 0
total_even = 0
total_odd = 0
divisible_by_3_and_5 = 0

for i in range(1, N + 1):

    sum_all = sum_all + i

    if i % 2 == 0:
        sum_even = sum_even + i
        total_even = total_even + 1

    else:
        sum_odd = sum_odd + i
        total_odd = total_odd + 1

    if i % 3 == 0 and i % 5 == 0:
        divisible_by_3_and_5 = divisible_by_3_and_5 + 1


print("Sum of all numbers:", sum_all)
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
print("Total even numbers:", total_even)
print("Total odd numbers:", total_odd)
print("Numbers divisible by both 3 and 5:", divisible_by_3_and_5)