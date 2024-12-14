# set is collection of object and in pyhton everything is object
# set contains unique elemnts
# set are unorder doesnit conatins index
# {} are used

s={"tarun","vicky","amit","tarun"}
print(s)

# for looop in set
for i in s:
    print(i)

s1={2,4,6}
s2={1,3,5}
print(s1.union(s2))


print(s2.update(s1))#update s1 with value of s2

s3={2,1}
print(s3.intersection(s2))  #commom value in both

print(s3.difference(s1))  #only prest in s3 specific 