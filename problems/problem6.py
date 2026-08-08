
def sum_of_squares(n):
    squares = [i**2 for i in range(n + 1)]
    return sum(squares)

def square_of_sum(n):
    series = [i for i in range(n + 1)]
    return sum(series)**2

print(square_of_sum(100) - sum_of_squares(100))