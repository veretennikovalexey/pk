class Flyable:
    def move(self):
        print('Летит')


class Swimmable:
    def move(self):
        print('Плывёт')


class Duck(Flyable, Swimmable):
    def __init__(self, on_water):
        self.on_water = on_water

    def move(self):
        if not self.on_water:
            Flyable.move(self)
        else:
            Swimmable.move(self)