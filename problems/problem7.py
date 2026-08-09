from math import sqrt
def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    i = 0
    for j in range(1, n**2, 2): #odds only
        if is_prime(j):
            i += 1
            if i == n:
                return j
    return 2


print(nth_prime(10001))



