l=["apple","mango","grapes","banana"]
for i in l:
    print(i)



def sum(list):
    total=0
    for i in list:
        total+=i
    return total
print(sum([1,2,4,6]))


def sumeven():
    ls=[]
    for i in range(1,10):
        if(i%2==0):
            ls.append(i)
    return ls

print(sumeven())