def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = str(factorial(100))

digits = []

for i in num:
    digits.append(int(i))

print(sum(digits))