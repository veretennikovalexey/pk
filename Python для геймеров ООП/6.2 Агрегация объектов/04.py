class Effect:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def apply(self):
        print(f"Эффект {self.name} длится {self.duration} секунд ☠️")


class Item:
    def __init__(self, name, effect=Effect("Отравление", 5)):
        self.name = name
        self.effect = effect

    def use(self):
        print(f"{self.name} используется!")
        if self.effect:
            self.effect.apply()
        else:
            print("...но ничего не происходит.")

poison = Effect("Отравление", 5)
apple = Item("Яблоко")

apple.use()