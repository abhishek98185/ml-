import numpy as np

arr = np.array([10, 20, 30, 40])
print("Array:", arr)

ref = arr
ref[2] = 99
print("After reference change:", arr)
copy_arr = arr.copy()
copy_arr[0] = 5
print("Copied array:", copy_arr)
mat = np.array([
    [5, 6, 7],
    [8, 9, 10]
])

print("Matrix:\n", mat)

print("Even index values:")
for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])

print("Element at (1,1):", mat[1][1])

print("Max value:", np.max(arr))
print("Min value:", np.min(arr))
print("Sum:", np.sum(arr))

print("Clipped:", arr.clip(15, 50))