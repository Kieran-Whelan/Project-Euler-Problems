def is_pythagorean_triple(x,y,z):
    if x**2 + y**2 == z**2:
        return True
    return False

# x < y < z

for i in range(1000, 1, -1):
    for j in range(i, 1, -1):
        for k in range(j, 1, -1):
            if i + j + k == 1000 and is_pythagorean_triple(k, j, i):
                print(k, j, i) #x y z
                print(k*j*i)