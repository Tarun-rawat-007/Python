numbers=[1,2,3,4,5,6,7,8,9]
even=map(lambda x : x%2==0,numbers)
print(list(even))
even=filter(lambda x : x%2==0,numbers)
print(list(even))