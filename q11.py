pythagorean_triples = [(a, b, c) for a in range(1, 10) for b in range(a, 10) for c in range(b, 10) if a**2 + b**2 == c**2]
print(pythagorean_triples)
