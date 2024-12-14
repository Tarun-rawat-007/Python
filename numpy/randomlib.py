import numpy as np

arr=np.array([1,2,3,4,5])
print(arr[1:5])
print("array diemsion:",arr.ndim)
arr2 = np.array([6,7,8, 9,10]) 
print(arr)
x=np.random.randint(2,10)
print(x)
# operation on arrray
print(np.add(arr, arr2))
print(np.subtract(arr, arr2))
print(np.multiply(arr, arr2))
print(np.divide(arr, arr2))
# compute square of each item
arr3=[1,2,3]
print("square of each item is:",np.square(arr3))

# craete 2d arr
arr4=np.array([[1,2,3],[4,5,6]])
print(arr4[0][1])
# 2d martix and its tranpose
arr5=np.array([[1,2,3],[4,5,6]])
print("Tranpose of matrix is:\n",np.transpose(arr5))

# createing 1 d array of 12 elemnt and reshape it to 2X3 matrix
arr6=np.arange(12)
print("Arange arry of 6:",arr6)
arr2X6=arr6.reshape(2,6)
print("Reshape array:\n",arr2X6)
# replace element greater that 35
arr7=np.array([12,34,56,34,23,22,34,45,23,26,56])
arr7[arr7>30]=0
print(arr7)
# compute men medianmode
arr8=np.array([3,4,5,7,8])
print("mean of array:",np.mean(arr8))
print("medianof array:",np.median(arr8))

