class BMW:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car..")

    def stop(self):
        print("Stopping the car..")


class ThreeSeries(BMW):
    
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def start(self): #Overridden the start method in the parent class: BMW
        super().start()
        print("Button Start")


class FiveSeries(BMW):
    
    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


threeSeries = ThreeSeries(True, "BMW", "328i", "2018")
fiveSeries = FiveSeries(True, "Ford", "Focus", "2008")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()

fiveSeries.start()
fiveSeries.stop()
