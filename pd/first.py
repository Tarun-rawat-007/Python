import numpy as np
import pandas as pd

dic={
    "name":['tarun','vicky','rohan','vivek'],
    "marks":[98,76,89,67],
    "city":["dheradun","mumbai","jummu","channai"]
}
df=pd.DataFrame(dic)
print(df)
df.to_csv('first.csv',index=False)   #import to excel csv
head=df.head(2)   #first 2 row head
print(head)
ser =pd.Series(np.random.random(10))
print(type(ser))
print(ser)