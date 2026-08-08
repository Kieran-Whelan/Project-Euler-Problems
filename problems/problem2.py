#fibonacci evens sum


def is_even(num):
    return num % 2 == 0

evens = []

n_0 = 1
n_1 = 1

n = 0

while n < 4000000:
    n = n_0 + n_1
    n_0 = n_1
    n_1 = n

    if is_even(n):
        evens.append(n)

print(sum(evens))