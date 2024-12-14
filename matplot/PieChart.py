import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

name=np.array(["bangla","iran","pakistan",'india',"usa","japan"])
population=np.array([20,10,40,90,80,60])


plt.pie(population,labels=name,autopct="%1.2f%%")

plt.xlabel("Names of Student")    #used for plotint x,y labels at Side
plt.ylabel("Marks of Student")

plt.show()
