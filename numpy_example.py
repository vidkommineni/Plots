import numpy as np

# array a ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# arange() decides the length of the array and reshape(row, colum) is the shape it takes
a = np.arange(12).reshape(3, 4)
print(f'A =  {a}')
print()

# array b ~~~~~~~~~~~~~~~~~~~~~~~~~~~
b = np.arange(8).reshape(4, 2)
print(f'B =  {b}')
print()

# array c ~~~~~~~~~~~~~~~~~~~~~~~~~~~
c = np.arange(6).reshape(2, 3)
print(f'C = {c}')
print()

# array d ~~~~~~~~~~~~~~~~~~~~~~~~~~~
d = a @ b @ c  # using @ does a matrix product instead of multiplying each element
print(f'D = {d}')
print()

# array d^t ~~~~~~~~~~~~~~~~~~~~~~~~~~~
dt = d.transpose()  # transposing an array reflects the elements across the middle diagonal
print(f'D^T = {dt}')
print()

# array e ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# using operators like * and / apply to each element in the array instead of a matrix product or quotient
e = (d**(1/2)) / 2
print(f'E = {e}')
