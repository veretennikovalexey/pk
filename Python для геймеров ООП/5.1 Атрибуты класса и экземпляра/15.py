class Planet:
    ''' Гравитация. Часть 2 '''
    gravity = 9.8

    def __init__(self, name):
        self.name = name

earth = Planet("Earth")
mars = Planet("Mars")

mars.gravity = 3.73


print(earth.gravity)
print(mars.gravity)
print(Planet.gravity)