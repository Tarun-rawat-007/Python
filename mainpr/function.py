def check(age):
    if(age<18):
        return "tennager"
    elif(age>=18):
        return "adult"
    else:
        return "invalid age"
    
print(check(14))

def check2(a,b,c):
    if(a>b) and(a>c):
        return a
    elif(b>a) and (b>c):
        return b
    else:
        return c

print("largest among threee number:",check2(2,32,14))

def grade(marks):
    if(marks>90):
        return "A"
    elif(marks>80) and(marks<90):
        return "B"
    elif(marks>60) and(marks<80):
        return "C"
    else:
        print("Fail")

print("hea has obtained :",grade(78))

