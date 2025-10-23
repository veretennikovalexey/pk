class Hero:
    def __init__(self, name, hero_class, health, armor, damage):
        self.name = name
        self.hero_class = hero_class
        self.health = health
        self.armor = armor
        self.damage = damage

    
    def show_info(self):
        print( F'''\
=== Создание героя ===

Имя: {self.name}
Класс: {self.hero_class}
Здоровье: {self.health}, Броня: {self.armor}, Урон: {self.damage}''')        

name, hero_class, health, armor, damage = input(), input(), int(input()), int(input()), float(input())

hero = Hero(name, hero_class, health, armor, damage)
hero.show_info()
