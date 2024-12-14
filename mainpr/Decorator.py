# def decor(printer):
#     def inner():
#         printer()  #execeting fuctinalty
#         print("welcome 1")
#     return inner
# @decor
# def printer():
#     print("welcome2")
#     print("welcome3")


# printer()

# example 2

# def decor(addition):
#     def inner():
#         result=addition()
#         num3=int(input("Enter num3:"))
#         result=result+num3
#         return result
#     return inner
# @decor
# def addition():
#     num1=int(input("Enter num1:"))
#     num2=int(input("Enter num2:"))
#     result=num1+num2
#     return result

# print("addition of numer is",addition())



# new program
def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()