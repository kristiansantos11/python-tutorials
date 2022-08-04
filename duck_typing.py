#POLYMORPHISM SIMPLE EXAMPLE
class Duck:
    def talk(self):
        print("QUACC")


class Human:
    def talk(self):
        print("Human says 'hai'")


def callTalk(obj):
    obj.talk()
    
d = Duck()
h = Human()
callTalk(d)
callTalk(h)
