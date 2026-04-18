# Q19: Demonstrate use of iterators

# Create a list
my_list = [10, 20, 30, 40]

# Create an iterator object using iter()
my_iterator = iter(my_list)

print("Using next() to iterate:")

# Access elements using next()
try:
    print(next(my_iterator))  # 10
    print(next(my_iterator))  # 20
    print(next(my_iterator))  # 30
    print(next(my_iterator))  # 40

    # This will raise StopIteration
    print(next(my_iterator))

except StopIteration:
    print("End of iterator reached!")