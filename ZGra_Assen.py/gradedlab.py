# Write a Python function that calculates the factorial of a number. Ensure that the function can take an optional argument to decide whether the result should be printed or returned.
import math

def factorial(num, print_result=False):
    result = math.factorial(num)
    
    if print_result==True:
        print(f"The factorial of {num} is {result}")
    else:
        return result


factorial(5, print_result=True)  
factorial(5) 




# Write a Python program that defines a decorator to log the execution time of a function that calculates the sum of all numbers from 1 to 1000000. 
import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()  
        result = func(*args, **kwargs)
        end = time.time()    
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@log_time
def calculate_sum():
    return sum(range(1, 1000001))

# calculate_sum()



# Write a program that generates a dictionary where keys are numbers between 1 and 10, 
# and the values are the squares of the keys.
squares = {i: i**2 for i in range(1, 11)}
# print(squares)
