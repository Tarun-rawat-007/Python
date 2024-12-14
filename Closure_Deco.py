
# closure in python # inner function acced outer function variable that is not in its memory
def outer():
    x=12
    def inner():
        print("Closure x value:",x)
    inner()
outer()

# Decorator Function   #a function that take an function and return by adding some funcnality
def dec(add):
    def inner():
        c=5
        return add()+c
    return inner
@dec   # this is property neccesarry need 
def add():
    a,b=2,3
    return a+b
print("Decorator fun: ",add())