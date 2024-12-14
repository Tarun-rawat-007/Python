import numpy as np

arr=np.array([1,2,3,4,5,6])
print(arr)
print("Elemnt at 0 Index ",arr[0])
print("sum of ele at index 0,1:",arr[1]+arr[2])
print(type(arr))

arr2d=np.array([[1,2,3],[4,5,6]])
print("2d array:\n",arr2d)
print('3th element on 2nd row: ', arr2d[1, 2])
arr3d =np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("3sarray:\n",arr3d)


# functions
print("Dimesion of array: ",arr3d.ndim)
