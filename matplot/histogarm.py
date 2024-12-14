import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


arr=np.array([34,56,34,56,31,45,87,39,32,57,23,23,22,1,4,6,7,57,58,11,17])


plt.hist(arr,bins=[0,10,20,30,40,50,60])

plt.xlabel("Names of Student")    #used for plotint x,y labels at Side
plt.ylabel("Marks of Student")

plt.show()
