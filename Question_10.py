# Q10: Find second largest and second-smallest elements without using built-in functions

# Input list
nums = [12, 5, 8, 20, 3, 15]

# Step 1: Initialize variables
largest = second_largest = float('-inf')  # smallest possible value
smallest = second_smallest = float('inf')  # largest possible value

# Step 2: Traverse the list
for num in nums:

    # ---- Find largest and second largest ----
    if num > largest:
        second_largest = largest  # update second largest
        largest = num  # update largest
    elif num > second_largest and num != largest:
        second_largest = num  # update second largest

    # ---- Find smallest and second smallest ----
    if num < smallest:
        second_smallest = smallest  # update second smallest
        smallest = num  # update smallest
    elif num < second_smallest and num != smallest:
        second_smallest = num  # update second smallest

# Step 3: Display results
print("List:", nums)
print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)

lst = [10, 5, 20, 8, 15]

lst = list(set(lst))   # remove duplicates
lst.sort()

print("Second Smallest:", lst[1])
print("Second Largest:", lst[-2])