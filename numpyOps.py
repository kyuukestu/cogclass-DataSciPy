import numpy as np

a = np.array([1,-1])
b = np.array([1,1])

# print(a*b)
# print(np.dot(a,b))

a = np.array([0,1,2,3,4])

for e in range (len(a)):
    print(f"a[{e}]:", a[e])
    
print(np.__version__)

print("Type of a and data type of its elements:", type(a), "&",a.dtype)

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

print("Type of b and data type of its elements:", type(b), "&", b.dtype)

c = np.array([20, 1, 2, 3, 4])
print("Array c:", c)

c[0] = 100
print("Array c, first index changed:", c)

c[3:5] = 300, 400
print("Array c, 3rd and 4th index changed:", c)

arr = np.array([1,2,3,4,5,6,7])
print("Array printed by defining the steps in slicing, [start:end:step]:",arr[1:5:2])
print("Start is assumed to be 0 if not passed in: ", arr[:4])
print("End is assumed to be the length of the array if not passed in: ", arr[4:])
print("Step is assumed to be 1 if not passed in: ", arr[1:4])
print("Step can be negative: ", arr[4:1:-1])

# List can be used to select more than one index
select = [0, 2, 3, 4]

d = c[select]
print("Array d:", d)

c[select] = 100000
print("Array c, selected index changed:", c)

# Where shape is a tuple of integers indicating the size of the array in each dimension
print("Size & # of dimensions & shape:", a.size, a.ndim, a.shape)

a = np.array([1, -1, 1, -1])
mean = a.mean()
print("Mean of a:", mean)

std_dev = a.std()
print("Standard deviation of a:", std_dev)

b = np.array ([-1, 2,3, 4, 5])
max_b = b.max()
print("Max of b:", max_b)

min_b = b.min()
print("Min of b:", min_b)

# Array addition
u = np.array([1,0])
v = np.array([0,1])

z = np.add(u, v)
print("Sum of arrays:", z)