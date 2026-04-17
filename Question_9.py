# Q9: List operations demonstration

# Initial list
my_list = [10, 20, 30]

print("Original List:", my_list)

# Append: adds element at end
my_list.append(40)
print("After append(40):", my_list)

# Insert: adds element at specific index
my_list.insert(1, 15)
print("After insert(1, 15):", my_list)

# Extend: adds multiple elements
my_list.extend([50, 60])
print("After extend([50, 60]):", my_list)

# Remove: removes specific value
my_list.remove(20)
print("After remove(20):", my_list)

# Pop: removes element by index (default last)
popped = my_list.pop()
print("After pop():", my_list)
print("Popped Element:", popped)

# Sort: sorts list in ascending order
my_list.sort()
print("After sort():", my_list)

# Reverse: reverses the list
my_list.reverse()
print("After reverse():", my_list)