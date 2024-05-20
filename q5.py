def fibonacci_generator():
    a, b = 0, 1
    for _ in range(7):
        yield a
        a, b = b, a + b

# Example usage
fib_gen = fibonacci_generator()
for number in fib_gen:
    print(number)
