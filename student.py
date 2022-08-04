class Student:
    major = "CpE"

    def __init__(self, stud_id, name):
        self.stud_id = stud_id
        self.name = name

print("MAJOR: " + Student.major) # static class attributes can be accessed without instantiating the class itself.

s1 = Student(181, "John")
s2 = Student(111, "Bill")


print(s1.major)
print(s1.name)
print(str(s1.stud_id) + "\n")

print(s2.major)
print(s2.name)
print(str(s2.stud_id) + "\n")
