import numpy as np
M1 = np.array([ [9, 12], [23,30] ])
print(M1)

u = np.array([2, 1])
tichM1u=M1.dot(u)
print(tichM1u)

tichuM1 = u.dot(M1)
print(tichuM1)

print(np.dot(M1, u))

print("\n")

mat1 = np.zeros( [5,5])
print(mat1)
mat2 = np.ones( [5,5])
print(mat2)
mat3 = mat1 + 2* mat2
print(mat3)
mat4 = mat3
mat3[3][2] = 10
print(mat3)
print(mat4)
print("Vì gán tham chiếu mat4 cho mat3 nên cả hai cùng thay đổi.")
mat5 = np.copy(mat3)
mat3[3][2] = 10
print("mat3 thay đổi nhưng mat5 không thay đổi vì là bản sao.")
mat6 = np.empty([4, 5])
print(mat6)
mat7 = np.identity(4)
print(mat7)
mat8 = np.random.random([4,5])
print(mat8)
