numbers=[1,2,3,4,5,6,7,8,9]     
newoddlist=lambda x:x%2!=0
oddnumbers=list(filter(newoddlist,numbers))
print(oddnumbers)

square=lambda x:x*x    #build sqaure lambda function
squareodd=list(map(square,oddnumbers))   #map implemnt sqare function to all element
print(squareodd)




# The map function applies a given function to every element in a sequence and returns an iterator (or list) of the results.
li2 = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, li2))
print("map function",squares)


# The filter function is used to filter elements from a sequence (such as a list or tuple) based on a condition. It applies a function that returns True or False to each element in the sequence and keeps only the elements where the function returns True.
li3=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,li3))
print(even)


# reduce function  takes a function and applies it cumulatively to the items of a sequence (such as a list and  reduce the sequence to a single value.
from functools import reduce
li=[1,2,3,4]
sum=reduce(lambda x,y:x+y,li)
print("reduce output:",sum)



