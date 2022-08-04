class Car:
    def __init__(self, manufacturer, year):
        self.manufacturer = manufacturer
        self.year = year

    class Engine:
        def __init__(self, id_number):
            self.number = id_number

        def start(self):
            print("Engine Started.")

c1 = Car("BMW", 2017)
e = c1.Engine(2017101)
e.start()

#create an instance of the outer class
#before creating an instance of the inner class
