class myclassname:  #class
    def __init__(self,name,age):  #init costructer typr rurn automatically
        self.name=name
        self.age=age
    


obj=myclassname("tarun",22)    #class object
print(obj.name)
print(obj.age)

class extendesChild(myclassname):
    pass
