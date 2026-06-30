import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("array: " ,arr)
print("shape: " , arr.shape)
print("size: ", arr.size)
print("no. of dimensions: ", arr.ndim)
print("first row: ", arr[0])
print("second row: ", arr[1])
print("first coloumn: ", arr[:,0])
print("third row: ", arr[:,2])
print("element 5: ", arr[1][1])
print("element 9: ", arr[2][2])
