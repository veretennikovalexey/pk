class Sword:
    def use(self, power):
        print(f"Меч наносит {power} урона!")


class Hammer:
    def use(self, power):
        print("Молот бьёт по земле!")


class Bow:
    def use(self, power, speed=1):
        print(f"Лук выпускает стрелу силой {power} и скоростью {speed}.")


def activate(item):
    item.use(5)

activate(Sword())
activate(Hammer())
activate(Bow())