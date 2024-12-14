def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b!=0):
        return a/b
    else:
        return "b is 0"

num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))

print("select opertaion:")
print("1 for add:")
print("2 for sub:")
print("3 for multiply:")
print("4 for divide:")
op=int(input("Enter a Operation[+ - * /]:"))
if(op==1):
    print(f"sum of number is",add(num1,num2))
elif(op==2):
    print("sub of number is",sub(num1,num2))
elif(op==3):
    print("mul of number is",mul(num1,num2))
elif(op==4):
    print("div of number is",div(num1,num2))