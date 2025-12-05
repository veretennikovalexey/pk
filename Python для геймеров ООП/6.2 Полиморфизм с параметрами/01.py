# Пример 1. Полиморфизм с параметром

class Bow:
    def use(self, power):
        print(f"Лук выпускает стрелу силой {power}!")


class Wand:
    def use(self, power):
        print(f"Посох усиливает заклинание на {power} ед!")


class Trap:
    def use(self, power):
        print(f"Ловушка срабатывает с силой {power}!")


def activate(item):
    item.use(10)


activate(Bow())
activate(Wand())
activate(Trap())

# Пример 2. Полиморфизм, даже если методы выглядят по-разному

class Wand:
    def use(self, power, speed=1):
        print(power, speed)


class Staff:
    def use(self, *args):
        print(args)


class Totem:
    def use(self, *args, **kwargs):
        print(args, kwargs)


def activate(item):
    item.use(10)


activate(Wand())
activate(Staff())
activate(Totem())


