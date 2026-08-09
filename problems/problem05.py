#only need to check numbers divisible by 20


def is_evenly_divisible(number): #evenly divisible by numbers 1-20
    for i in range(1, 20):
        if number % i == 0:
            continue
        else:
            return False
    return True

#100000 arbitrary
for i in range(0, 1000000000, 20):
    if is_evenly_divisible(i) and i != 0:
        print(i)
        break