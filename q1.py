def prime_generator():
    primes = []
    candidate = 2
    while True:
        is_prime = all(candidate % p != 0 for p in primes)
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 1

# Example usage
gen = prime_generator()
for _ in range(10):
    print(next(gen))
