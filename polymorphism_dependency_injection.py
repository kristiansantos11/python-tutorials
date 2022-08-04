class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()


class AirbusEngine:
    def start(self):
        print("Starting AirBus engine...")


class BoeingEngine:
    def start(self):
        print("Starting Boeing engine...")


abe = AirbusEngine()
f = Flight(abe)
f.startEngine()

be = BoeingEngine()
f1 = Flight(be)
f1.startEngine()
