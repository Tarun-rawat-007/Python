# import is process of loding code from python module to current script
# creation of virtual environemt for importing version,pandas
# 1=python -m venv myenv   #craete a folder myenv-a copy 
# 2=myenv\Scripts\activate    #activate it(myenv) shown
# 3=pip install pandas          #instal packages
import pandas as pd   #pd given a shortcut by keyword 'as'
import math
from math import sqrt,pi   #for importing pi and sqrt
from math import *   #for importing all function

a=math.floor(4.3432)
print(a)

b=sqrt(9)*pi
print(b)

print(dir(math))    #gives all method math consist 'dir'