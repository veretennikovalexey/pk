class Plant:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
class Zombie:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self, plant):
        print(f'{self.name} кусает {plant.name}!')
        plant.hp = max(plant.hp - self.damage, 0)
        print(f'У {plant.name} осталось {plant.hp} прочности.')
        return plant.hp > 0

*plant_name , plant_hp  = input().split() # подсмотрел у ребят
*zombie_name, zombie_hp = input().split()

p = Plant (' '.join(plant_name ), int(plant_hp ))
z = Zombie(' '.join(zombie_name), int(zombie_hp))

while z.attack(p):
    pass