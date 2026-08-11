#lattice paths

#combinatorics
#

from math import factorial

paths = factorial(40)/(factorial(20)*factorial(40-20))

print(int(paths))