x=4
print("Global x:",x)

def hello():
    global x                     # bcs of this global x also changes
    x=5
    print("local x:",x)

hello()
print("Global x:",x)     #global x also chnages