#triangular numbers

nums = []

for i in range(1, 10000 + 1):
    tri = 0
    for j in range(1, i + 1):
        tri += j
    nums.append(tri)

print("List done")

for num in nums:
    factors = 0
    if num % 2 == 0:
        for i in range(1, num + 1):
            if num % i == 0:
                factors += 1
        if factors > 500:
            print(num)
            break