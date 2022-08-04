class Student:
    
    def setId(self,stud_id):
        self.stud_id = stud_id

    def getId(self):
        return self.stud_id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


s = Student()
s.setId(123)
s.setName("Ian")

print(s.getId())
print(s.getName())

'''

This is encapsulation

Setter methods are used to set class attributes
Getter methods are used to access those attributes

'''
