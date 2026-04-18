# Q30: Password validation

import re

password = input("Enter password: ")

# At least 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")