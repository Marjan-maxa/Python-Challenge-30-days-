text = input("Enter a string: ")

# Reverse
reverse_text = ""

for char in text:
    reverse_text = char + reverse_text

print("Reverse:", reverse_text)


# Palindrome
original = ""

for char in text:

    if char != " ":
        original = original + char.lower()


reverse_text = ""

for char in original:
    reverse_text = char + reverse_text


if original == reverse_text:
    print("Palindrome")
else:
    print("Not Palindrome")