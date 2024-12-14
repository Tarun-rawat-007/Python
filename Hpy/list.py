# list is like array ordered collection seprated by comma, and enclosed in []
# list are mutable and can be changed  
l=[1,2,3,4,"tarun"]
print(l)
print(type(l))
if "tarun" in l:
    print("true")
else:
    print("not true")
# methods of list
li=[1,32,1,33,44,35,64,7,8,9,10]
print(li)
li.append(11)   #append at last
print(li)
li.sort()    #sort
print(li)
li.sort(reverse=True)    #sort in reverse order
print(li)
li.reverse()
print(li)
print(li.count(1))# count 1 
l2=li.copy()
print(l2)
l2.insert(2,89)#insert ele at specific index
print(l2)
k=li+l2   #concatination of list
print(k)
