import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


india=[25,47,56,44,34,67,78,11]
pak=[65,17,34,54,14,77,98,81]

scorerange=[5,10,15,20,25,30,35,40]

plt.scatter(india,scorerange,color='b')
plt.scatter(pak,scorerange,color='g')

plt.xlabel("Names of Student")    #used for plotint x,y labels at Side
plt.ylabel("Marks of Student")

plt.show()