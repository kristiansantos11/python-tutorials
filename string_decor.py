def attach(func):
    def adder(s):
        result = func(s)
        result += " This is the added part!"
        return result
    return adder

@attach
def greet(name):
    return "Hello " + name

print(greet("Ian"))

#output should be:
# Hello This is the added part!
