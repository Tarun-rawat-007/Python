import numpy as np

array = np.arange(1, 10).reshape(3, 3)
print("Original Array:\n",array)


second_row = array[1,:]
print("\nSecond Row:", second_row)

third_column = array[:,2]
print("Third Column:", third_column)


transposed = array.T
print("\nTransposed Array:\n",transposed)


sum_of_elements = np.sum(array)
print("\nSum of all elements:", sum_of_elements)




