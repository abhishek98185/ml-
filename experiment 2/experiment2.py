import numpy as np


#creating and operations in 1-D array

a=np.array([18,45,7,73,20])
print(f"the dimension of array is : {a.ndim}")
print(f"the shape of arrray is : {a.shape} ")
print(f"the datatype in array is : {a.dtype}")


#creating and operations on 2-D array

b=np.array([[18,45,7,73,20],[26,15,2,20,9]])
print(b)
print("reshaping the 2-D array")
bb=b.reshape((5,2))
print(bb)

print(f"the dimension of b is {b.ndim} and reshaped b is {bb.ndim}")
print(f"the shape of b is {b.shape} and reshaped b is {bb.shape}")



# ##operations on numpy array 
arr=np.array([10,2,11,23,2,3,44,2])
print(arr)
print(arr*5)
print(arr**3)

arr[1]=20
print(arr)



# # copy of array in numpy

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = arr1.reshape(2, 3).copy()

print("printing array 1:", arr1)
print("printing copy of array 2 with reshaping it:", arr2)

arr2[1, 2] = 10
print(arr2)


# # numpy array indexing 

d=np.array([0,0,0,0,0,0,0,0,0,0])
for i in range (0,10):
    if(i%2==0):
        d[i]=i
    else:
        d[i]=i+1
    
print(d)


# #clip() function in numpy 

e=np.array([100,23,20,342,553,54,35,255])
print(e)
print(e.clip(50,200))
