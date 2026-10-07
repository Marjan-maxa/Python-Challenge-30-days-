text = input("Enter a string: ")

characters = len(text)

alphabet_count = 0
digit_count = 0
space_count = 0
vowel_count = 0
consonant_count = 0
upper_count = 0
lower_count = 0

for char in text:

    if char.isalpha():
        alphabet_count = alphabet_count + 1

        if char.lower() in "aeiou":
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1

    if char.isdigit():
        digit_count = digit_count + 1

    if char == " ":
        space_count = space_count + 1

    if char.isupper():
        upper_count = upper_count + 1

    if char.islower():
        lower_count = lower_count + 1


print("\n--- String Analysis ---")
print("Total Characters:", characters)
print("Alphabet:", alphabet_count)
print("Digits:", digit_count)
print("Spaces:", space_count)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Uppercase:", upper_count)
print("Lowercase:", lower_count)