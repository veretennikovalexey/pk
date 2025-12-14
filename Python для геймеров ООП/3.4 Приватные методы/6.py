class Wizard:
    def __init__(self, energy):
        self.__energy = energy

    def __regenerate(self):
        self.__energy += 10

    def meditate(self):
        self.__regenerate()
        print(f"Энергия: {self.__energy}")

w1 = Wizard(50)
w2 = Wizard(11)
w1.meditate()
w2.meditate()