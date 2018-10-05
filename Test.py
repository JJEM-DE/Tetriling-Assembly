from copy import deepcopy

A = [4,5,6,9]

B = deepcopy(A)

B[2] = 123

print(A)
print(B)
