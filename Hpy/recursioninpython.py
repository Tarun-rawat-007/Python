def sum(a,b):
    sum=a+b
    return sum
print(sum(2,3))

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print("factorial:",factorial(5))
    