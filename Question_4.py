user_input = input("Enter a value: ")

# Try converting dynamically
try:
    value = int(user_input)
    print("Converted to Integer:", value)
except:
    try:
        value = float(user_input)
        print("Converted to Float:", value)
    except:
        if user_input.lower() == "true" or user_input.lower() == "false":
            value = user_input.lower() == "true"
            print("Converted to Boolean:", value)
        else:
            value = user_input
            print("Treated as String:", value)

print("Final Type:", type(value))