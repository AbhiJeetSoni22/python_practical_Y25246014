# Q12: Remove duplicates while maintaining order

data = [1, 2, 2, 3, 4, 3, 5, 1]

result = []
seen = set()

for item in data:
    if item not in seen:
        result.append(item)
        seen.add(item)

print("Original List:", data)
print("Without Duplicates:", result)