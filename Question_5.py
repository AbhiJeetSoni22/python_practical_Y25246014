# Given mixed list
mixed_list = [10, 3.14, "hello", True, 5, "world", 2.5,[1,2], (3,4)]

# Creating empty lists for each datatype
integers = []
floats = []
strings = []
booleans = []
lists = []
tuples = []

# Loop through each element in the list
for item in mixed_list:

    # Check if item is of type int
    # Note: bool is a subclass of int, so check bool first
    if isinstance(item, bool):
        booleans.append(item)

    elif isinstance(item, int):
        integers.append(item)

    # Check if item is of type float
    elif isinstance(item, float):
        floats.append(item)

    # Check if item is of type string
    elif isinstance(item, str):
        strings.append(item)
    # Check if item is of type list
    elif isinstance(item, list):
        lists.append(item)

    # Check if item is of type tuple
    elif isinstance(item, tuple):
        tuples.append(item)

# Print separated lists
print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)
print("Booleans:", booleans)
print("Lists:", lists)
print("Tuples:", tuples)