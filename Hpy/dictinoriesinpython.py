# key and value are stored 
# fast operations
# mapping used 
# are order collection
# eclosed in {}
d={
    1:"tarun",
    2:"vicky",
}

print(d)
print(d[1])     #throw error when ele not found
print(d.get(1))  #doesnt throw error when ele not found
print(d.keys())
print(d.values())

for i in d.keys():
    print(d[i])
    
dic1={"a":"tarun",
     "b":"vicky",
     "c":"amit",
     "d":"ram",
        }
dic2={"e":"priya",
     "f":"riya",
     "g":"sonia",
     "h":"kelly",
        }
dic1.update(dic2)    #updated d=ictonary
print(dic1)


dic2.clear()#empty dic
print(dic2)

dic1.popitem()#delete last from dic
print(dic1)
dic1.pop("c")#delete specific from dic
print(dic1)
