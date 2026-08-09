from math import sqrt
"""
def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [2]

for i in range(3, 2000000, 2): #checking odds only
    if is_prime(i):
        print(i)
        primes.append(i)

print(sum(primes))
"""

#sieve of Eratosthenes

limit = 2000000
cross_limit = sqrt(limit)
sieve = [False for i in range(2, limit + 1)]

for n in range(4, limit, 2): #mark evens
    sieve[n] = True

for n in range(3, int(cross_limit) + 1, 2):
    if not sieve[n]:
        for j in range(n*n, limit-1, 2*n):
            sieve[j] = True

sum = 0
for n in range(2, limit-1):
    if not sieve[n]:
        sum += n

print(sum)