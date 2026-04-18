# Q29: Regex validation

import re

email = input("Enter email: ")
phone = input("Enter phone: ")

# Email pattern
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Phone pattern (10 digits)
phone_pattern = r'^\d{10}$'

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

if re.match(phone_pattern, phone):
    print("Valid Phone")
else:
    print("Invalid Phone")