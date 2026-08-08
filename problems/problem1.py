# multiples of 3 or 5
from decorator import append


def is_multiple(n):
    if n % 5 == 0:
        return True
    elif n % 3 == 0:
        return True
    else:
        return False

multiples = []
for i in range(1,1000):
    if is_multiple(i):
        multiples.append(i)

print(sum(multiples))