class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health


hero = Character("Карлах",100)

rules = {
    "name": "Имя",
    "health": "Здоровье"
}

for field, title in rules.items():
    print(title, getattr(hero, field))
