class boy:
    def say(self):
        print("I am a boy")

class family(boy):
    def say(self):
        super().say()
        print("i am father here")


class work(boy):
    def say(self):
        print("i am worker here")




ob1=family()
ob1.say()
ob2=work()
ob2.say()