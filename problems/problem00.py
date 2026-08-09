#sum of odd square numbers

def is_ood(num = int):
    if num % 2 != 0:
        return True
    else:
        return False

odd_squares = []

for i in range(1, 161000):
    if is_ood(i**2):
        odd_squares.append(i**2)

print(sum(odd_squares))
