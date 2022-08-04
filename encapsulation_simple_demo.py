class Student:
    def __init__(self):
        self.__id = 123
        self.__name = "Ian"

    def display(self):
        print(self.__id)
        print(self.__name)


s = Student()
s.display()

# Puting two underscores before a variable/method sets it as
# PRIVATE.

# THIS IS NAME MANGLING:
# syntax: _ClassName__field name or method name

#print(s._Student__id)
