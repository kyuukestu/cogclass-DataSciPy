import numpy as np
A = np.array([[11, 12], [21, 22], [31, 32]])
print(type(A))
print(A.shape)
print(A.dtype)

A = np.array([[11,12],[21,22]])
B = np.array([[1, 0], [0, 1]])

C = np.multiply(A, B)
print(C)

D = np.array([[0, 1], [1,0]])

I = np.dot(A, B)
print(I)

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)

X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]]) 

Z = X + Y