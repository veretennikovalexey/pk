# Пример 1. 🦆 Утиная типизация (duck typing)

class Pickaxe:
    def use(self):
        print("Кирка добывает руду!")

class Shovel:
    def use(self):
        print("Лопата копает землю!")

class Axe:
    def use(self):
        print("Топор рубит дерево!")

tools = [Pickaxe(), Shovel(), Axe()]

for tool in tools:
    tool.use()

# Пример 2. Полиморфизм без цикла

class Pickaxe:
    def use(self):
        print("Кирка добывает руду!")

class FishingRod:
    def use(self):
        print("Удочка ловит рыбу!")

class Flint:
    def use(self):
        print("Огниво зажигает факел!")

def use_item(item):
    item.use()

use_item(Pickaxe())
use_item(FishingRod())
use_item(Flint())

# Пример 3. Полиморфизм через наследование

class Tool:
    def use(self):
        print("Какой-то инструмент используется...")

class Pickaxe(Tool):
    def use(self):
        print("Кирка добывает руду!")

class Shovel(Tool):
    def use(self):
        print("Лопата копает землю!")

class Axe(Tool):
    def use(self):
        print("Топор рубит дерево!")

inventory = [Pickaxe(), Shovel(), Axe(), Tool()]

for item in inventory:
    item.use()

# AttributeError: 'Stone' object has no attribute 'use'