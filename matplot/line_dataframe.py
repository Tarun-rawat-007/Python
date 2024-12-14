import matplotlib.pyplot as plt
import pandas as pd

df=pd.DataFrame({
    "name":["tarun","sahil","vicky",'rahul',"vikas"],
    "salary":[3000,2000,3000,2800,2200],
    "age":[21,22,21,19,22]
})
plt.plot(df["name"],df["age"])

plt.title("Age Graph:")
# plt.title("Age Graph:",loc="left")
# plt.title("Age Graph:",loc="right")

plt.grid()   #grid is visiible aslo


plt.xlabel("Names of Student")    #used for plotint x,y labels at Side
plt.ylabel("Ages of Students(curr age)")

plt.show()
