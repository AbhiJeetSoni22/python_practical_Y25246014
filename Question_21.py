# Q21: Fibonacci using recursion and iteration with time comparison

import time

# Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Iterative Fibonacci
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 30

# Measure recursive time
start = time.time()
print("Recursive Result:", fib_recursive(n))
print("Recursive Time:", time.time() - start)

# Measure iterative time
start = time.time()
print("Iterative Result:", fib_iterative(n))
print("Iterative Time:", time.time() - start)