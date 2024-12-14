def outer():
    print("hello")
    def inner():
        x=120
        return x
    return inner

inner=outer()
print(inner())
