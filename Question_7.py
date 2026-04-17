# Q7: Count vowels, consonants, digits, and special characters

# Take input string
text = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
digits = 0
special = 0

# Define vowels
vowel_set = "aeiouAEIOU"

# Loop through each character
for char in text:
    if char.isalpha():  # check if alphabet
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():  # check if digit
        digits += 1
    else:
        special += 1  # everything else

# Print results
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)