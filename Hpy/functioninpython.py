a=5
b=4
# mutiply=a*b

def multplyfun(a,b):
    multiply=a*b
    print(multiply)

multplyfun(a,b)    #fumction call

def islesser(a,b):
    pass #keyword which tell to live function here and complete later

# function arguments in python
#4 types of arguments that can passed default,keyword,variable,required arguments
def average(a,b):
    print("the average is:",(a+b)/2)
average(2,3)

def average(a=1,b=3):
    print("the average is:",(a+b)/2)
average()
# keyword arguments
average(b=6,a=4) #doesnt concern for order
# required argumrents
average(a=2)    #b value taken default 3


# returning function
def sum(a,b):
    sum=a+b
    return sum

printsum=sum(2,3)
print("sum of numbers is:",printsum)