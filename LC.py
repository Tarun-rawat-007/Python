squares=[i**2 for i in range(1,6)]
print("squares of number:",squares)

even=[i for i in range(1,10) if(i%2==0)]
print("even number in 1-10:",even)

odd=[i for i in range(1,10) if(i%2!=0)]
print("odd number in 1-10:",odd)

words=["tarun","my","singh"]
wordleng=[len(i) for i in words]
print(wordleng)

string='my name is tarun rawat'
filteroutvow=[i for i in string if i not in 'aeiou']
print(filteroutvow)

div35=[i for i in range(1,101) if i%3==0 and i%5==0]
print(div35)
