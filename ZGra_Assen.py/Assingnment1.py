numbers= input("Enter a list of integers : ")
input_list = list(map(int, numbers.split()))

squared_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, input_list)))


print("Output:", squared_evens)
