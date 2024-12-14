import matplotlib.pyplot as plt
import numpy as np

a=np.arange(5)
b=[2,4,6,8,10]
c=[5,6,7,8,9]

fig=plt.figure()
ax=plt.subplot()

ax.plot(a,b,'k--',label='line b with x')
ax.plot(a,c,'k:',label='line c with x')
ax.legend()   #legend box
# legend is box on that consist all keys,symbols used





plt.grid()
plt.show()