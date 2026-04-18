# Q13: Dictionary operations using functions

students = {
    "A": 85,
    "B": 92,
    "C": 78,
    "D": 88
}

# Function to find topper
def find_topper(students_dict):
    topper = ""
    max_marks = -1

    for name, marks in students_dict.items():
        if marks > max_marks:
            max_marks = marks
            topper = name

    return topper, max_marks


# Function to calculate average marks
def calculate_average(students_dict):
    total = 0

    for marks in students_dict.values():
        total += marks

    avg = total / len(students_dict)
    return avg


# Function to sort students by marks using Bubble Sort
def sort_by_marks(students_dict):
    sorted_list = list(students_dict.items())

    # Bubble sort
    for i in range(len(sorted_list)):
        for j in range(0, len(sorted_list) - i - 1):
            if sorted_list[j][1] > sorted_list[j + 1][1]:
                # swap
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    return sorted_list


# ---- Function Calls ----
topper, max_marks = find_topper(students)
avg = calculate_average(students)
sorted_students = sort_by_marks(students)

# ---- Output ----
print("Topper:", topper, "Marks:", max_marks)
print("Average:", avg)
print("Sorted (by marks):", sorted_students)