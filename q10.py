squares = list(map(lambda x: x**2, range(1, 21)))
odd_squares = list(filter(lambda x: x % 2 != 0, squares))
print(odd_squares)
