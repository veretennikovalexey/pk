class Pokemon:
    def __init__(self, name, type, hp, attack):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack

    def show(self):
        print(f"{self.name} ({self.type}) — HP: {self.hp}, Атака: {self.attack}")

class FirePokemon(Pokemon):        
    def apply_bonus(self): 
        self.attack += 10

class WaterPokemon(Pokemon):        
    def apply_bonus(self): 
        self.hp += 15

class ElectricPokemon (Pokemon):        
    def attack_action(self):
        print(f'⚡ {self.name} выпускает молнию! Сила атаки: {self.attack}')