def geometric_progression(a, q):
    term = a
    while True:
        yield term
        term *= q

# Example usage
gp = geometric_progression(2, 3)
for _ in range(10):
    print(next(gp))
