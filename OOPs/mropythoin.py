class A:
    pass

class B(A):
    pass

class C(B):
    pass


# Print the Method Resolution Order for class D
print(C.mro())
