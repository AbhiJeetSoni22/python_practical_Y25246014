# Q20: Manual implementations

# Manual map()
def my_map(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result

# Manual filter()
def my_filter(func, data):
    result = []
    for item in data:
        if func(item):
            result.append(item)
    return result

# Manual reduce()
def my_reduce(func, data):
    result = data[0]
    for item in data[1:]:
        result = func(result, item)
    return result

# Test
nums = [1, 2, 3, 4]

print("Map (square):", my_map(lambda x: x*x, nums))
print("Filter (even):", my_filter(lambda x: x%2==0, nums))
print("Reduce (sum):", my_reduce(lambda x,y: x+y, nums))