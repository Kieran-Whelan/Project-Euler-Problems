"""
triangular numbers
can be computed using t_n = n(n+1)/2
n and n + 1 are co prime i.e only common divisor is 1
when n is even number of divisors of t_n = divisors of n/2 * divisors of n+1
when n is odd number of divisors of t_n = divisors of n * divisors of n+1/2
"""


def is_even(n):
    return n % 2 == 0

def count_divisors(n):
    count = 0
    for i in range(1, int(n + 1)):
        if int(n) % i == 0:
            count += 1
    return count

divisors = 0
n = 1
triangular_num = 0

while divisors < 500:
    triangular_num = (n* (n+1))/2
    if is_even(n):
        divisors = count_divisors(n/2) * count_divisors(n + 1)
    else:
        divisors = count_divisors(n) * count_divisors((n+1)/2)
    n += 1

print(int(triangular_num))
print(divisors)



