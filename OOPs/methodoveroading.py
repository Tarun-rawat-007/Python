def add(a, b, c=0):
    return a + b + c


print(add(2, 3))     # Output: 5 
print(add(2, 3, 4))  # Output: 9 

def add2(*args):
    return sum(args)

print(add2(2, 3, 4))  # Output: 9
print(add2(2, 3))     # Output: 5
print(add2(1, 2, 3, 4, 5))  # Output: 15