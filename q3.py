from itertools import compress

def first_n_odd_even(n):
    numbers = range(2*n)
    odd_selector = [(i % 2 != 0) for i in numbers]
    even_selector = [(i % 2 == 0) for i in numbers]
    odds = list(compress(numbers, odd_selector))
    evens = list(compress(numbers, even_selector))
    return odds[:n], evens[:n]

# Example usage
odds, evens = first_n_odd_even(10)
print('Odds:', odds)
print('Evens:', evens)
