a = "abc"
b=0

try:
    ans = int(a) / b
    print('Answer is:',ans)
except (ZeroDivisionError, ValueError) as e:
    print('Please enter number greater than zero:',e)