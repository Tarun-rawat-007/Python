# tupple are immutable not change
# circular bracket are used
# orderes set
t=(1,23,4,5,6)
print(type(t),t)
t2=(1,)    # comma, is nexxcceray in tuple (1,) ======(1)=X cannot be wrriten
print(t2)
if 32 in t:
    print("is present")
else:
    print("not present")
t3=(1,2,3,1,5,6,2,3,1,6)
coun=t3.count(1)
print(coun)
