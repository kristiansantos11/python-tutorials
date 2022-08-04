from abc import abstractmethod, ABC

class BMW(ABC): # this now becomes an interface class since
                # every method in this class is abstract.
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):
    
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def start(self): #Overridden the start method in the parent class: BMW
        super().start()
        print("ThreeSeries now starting...")

    def stop(self):
        super().stop()
        print("ThreeSeries stopping...")

    def drive(self):
        print("ThreeSeries is now being driven!")


class FiveSeries(BMW):
    
    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def start(self):
        super().start()
        print("Five series starting...")

    def stop(self):
        super().stop()
        print("Five series stopping...")

    def drive(self):
        print("FiveSeries is now being driven!")


threeSeries = ThreeSeries(True, "BMW", "328i", "2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.drive()
threeSeries.stop()

fiveSeries = FiveSeries(True, "BMW", "Coupe", "2011")
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)

fiveSeries.start()
fiveSeries.drive()
fiveSeries.stop()
