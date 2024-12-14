import re

text='''Tarun is a  good boy'''
pattern=r"[A-Z]+arun"


find=re.search(pattern,text)
print(find)

