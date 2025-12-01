# Пример 1. Базовая композиция: герой и предметы

class Item:
    def __init__(self, name, damage=0, heal=0):
        self.name = name
        self.damage = damage
        self.heal = heal

    def use(self):
        if self.damage > 0:
            print(f"{self.name} наносит {self.damage} урона 💥")
        elif self.heal > 0:
            print(f"{self.name} восстанавливает {self.heal} здоровья ❤️")
        else:
            print(f"{self.name} ничего не делает... 😅")

class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = [
            Item("Алмазный меч", damage=15),
            Item("Золотое яблоко", heal=20)
        ]
        print(f"Герой {self.name} появился в мире!")

    def show_inventory(self):
        print(f"🎒 Инвентарь {self.name}:")
        for i, item in enumerate(self.inventory, start=1):
            print(f"{i}. {item.name}")

    def use_all(self):
        print(f"{self.name} использует все предметы!")
        for item in self.inventory:
            item.use()            

hero = Character("Стив")

sword = Item("Алмазный меч", damage=15)
apple = Item("Золотое яблоко", heal=20)

hero.add_item(sword)
hero.add_item(apple)

hero.show_inventory()

# Пример 2. Более сложная композиция: предмет с эффектом

class Effect:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def apply(self):
        print(f"Эффект {self.name} длится {self.duration} секунд ☠️")

class Item:
    def __init__(self, name, damage=0, heal=0, has_poison=False):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.effect = Effect("Отравление", 5) if has_poison else None

    def use(self):
        print(f"{self.name} используется!")
        if self.damage > 0:
            print(f"{self.name} наносит {self.damage} урона 💥")
        elif self.heal > 0:
            print(f"{self.name} восстанавливает {self.heal} здоровья ❤️")
        if self.effect:
            self.effect.apply()

suspicious_stew = Item("Подозрительное рагу", has_poison=True)
suspicious_stew.use()

# Пример 3. Исчезновение объекта и его частей

class Familiar:
    def __init__(self, name):
        self.name = name
        print(f"Фамильяр {self.name} призван")

    def __del__(self):
        print(f"Фамильяр {self.name} растворяется в лёгкой дымке")


class Wizard:
    def __init__(self, name):
        self.name = name

        print(f"Маг {self.name} родился!")
        self.familiar = Familiar("Мрак")

    def __del__(self):
        print(f"Маг {self.name} умер!")

merlin = Wizard("Мерлин")
print("Удаляем мага...")
del merlin
