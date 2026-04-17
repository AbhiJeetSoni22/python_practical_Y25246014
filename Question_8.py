# Palindrome using slicing

text = input("Enter a string: ")

# Reverse using slicing
reverse_text = text[::-1]

# Check
if text == reverse_text:
    print("Palindrome")
else:
    print("Not Palindrome")
    

# Palindrome without slicing

text = input("Enter a string: ")

reverse_text = ""

# Manually reverse string
for char in text:
    reverse_text = char + reverse_text

# Check
if text == reverse_text:
    print("Palindrome")
else:
    print("Not Palindrome")