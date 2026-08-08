
def is_prime(n):
    factors = 0
    nums = [i for i in range(1, n+1)]
    for j in nums:
        if factors >= 3:
            return False
        if n % j == 0:
            factors += 1
    if factors == 2:
        return True

def nth_prime(n):
    i = 1 # 2 is only even prime
    for j in range(1, n**2, 2): #odds only
        if is_prime(j):
            i += 1
            if i == n:
                return j

print(nth_prime(10001))