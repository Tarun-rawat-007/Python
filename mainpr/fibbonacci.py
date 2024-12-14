def fibonacci(n):
    a,b=0,1
    while(a<=n):
        print(a,end=" ")
        a,b=b,a+b


fibonacci(10)

def fibbo(n):
    ls=[]
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        ls.append(a)
    return(ls)




print(fibbo(10))
