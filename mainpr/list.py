l=[1,2,3,4]
print(sum(l))
print(max(l))
print(min(l))
print(len(l))
l.append(5)
print("Appended item:",l)
l.remove(3)
print("Remved item:",l)
l.extend([7,3,9])
print("Sorted list:",sorted(l))
print(l)


print("Print value at index 3:",l[3])
print("Slicing list :",l[0:7:2])