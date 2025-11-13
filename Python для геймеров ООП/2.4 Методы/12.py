class Hero:
    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.hp = hp

    def train(self):
        self.power += 5
        print(f'+5 к силе {self.name}')            
        print(f'⚔️: {self.power}')            

    def rest(self):
        self.hp += 10
        print(f'+10 к hp {self.name}')            
        print(f'❤️: {self.hp}')            

