print("\n--- Immutable Example ---")
# Immutable example
my_tuple = (1, 2, 3)

print("Original tuple:", my_tuple)

# Trying to modify tuple (will give error)
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)

print("\n--- Mutable Example ---")

# Mutable example

my_list = [1, 2, 3]

print("Before modification:", my_list)

# Modifying list
my_list[0] = 10
my_list.append(4)

print("After modification:", my_list)