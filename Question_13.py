students = {
    "Aman": 85,
    "Riya": 92,
    "John": 78,
    "Neha": 88
}

# Topper
topper = ""
max_marks = -1

for name in students:
    if students[name] > max_marks:
        max_marks = students[name]
        topper = name

# Average
total = 0
count = 0
for marks in students.values():
    total += marks
    count += 1
avg = total / count

# Sorting (simple logic - bubble sort)
items = list(students.items())

for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

print("Topper:", topper, "-", max_marks)
print("Average:", avg)
print("Sorted:", items)

#SMALLER
# Create dictionary
students = {
    "Aman": 85,
    "Riya": 92,
    "John": 78,
    "Neha": 88
}

# 1. Find Topper
topper = max(students, key=students.get)

# 2. Find Average
total = sum(students.values())
avg = total / len(students)

# 3. Sort by Marks (ascending)
sorted_students = sorted(students.items(), key=lambda x: x[1])

# Output
print("Topper:", topper, "-", students[topper])
print("Average Marks:", avg)
print("Sorted by Marks:", sorted_students)