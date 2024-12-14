# nono graded lab 
# class Book:
#     def __init__(self,title,author,pages,year):
#         self.title=title
#         self.author=author
#         self.pages=pages
#         self.year=year
#     def printinfo(self):
#         print(f"book title: {self.title}")
#         print(f"book author: { self.author}")
#         print(f"book pages: {self.pages}")
#         print(f"book year: {self.year}")

# book=Book("life of pi","tarun","2123",2024)
# book.printinfo()

# question 2 
# def sum_expenses(expenses):
#     newdic={}

#     for k,v in expenses.items():
#         total_sum=sum(v)
#         newdic[k]=total_sum
#     return newdic

# expenses={
#     "food":[12,34,56],
#     "travel":[23,56,78],
#     "utilites":[23,76,34]
# }

# newdic=sum_expenses(expenses)
# print(newdic)

# question 3
# import numpy as np

# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("Normal array:\n",arr)

# tran=arr.T
# print("Transpose of an array:\n",tran)

# tran[[0,-1]]=tran[[-1,0]]
# print("swapping 1 row with last row :\n",tran)

# print("shape of array:",tran.shape)


