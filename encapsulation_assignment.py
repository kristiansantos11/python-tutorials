class Patient:
    def setID(self, patient_id):
        self.patient_id = patient_id

    def getID(self):
        return self.patient_id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSSN(self, ssn):
        self.ssn = ssn

    def getSSN(self):
        return self.ssn

patient1 = Patient()

patient1.setID(1)
print(patient1.getID())

patient1.setName("Ian")
print(patient1.getName())

patient1.setSSN(100)
print(patient1.getSSN())
