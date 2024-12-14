import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

name=np.array(["tarun","sahil","vicky",'rahul',"vikas",'riya'])
marks=np.array([80,60,76,40,60,70])


plt.bar(name,marks)

plt.xlabel("Names of Student")    #used for plotint x,y labels at Side
plt.ylabel("Marks of Student")

plt.show()
