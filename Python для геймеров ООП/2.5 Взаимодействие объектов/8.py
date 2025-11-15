class Player:
    def __init__(self, name, hp=100, armor=50, damage=20, shots=0):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.damage = damage
        self.shots = shots

    def attack(self, enemy, headshot=False):
        self.shots += 1
        headshot = (self.shots % 2 == 0)
    
        print(f'{self.name} стреляет в {enemy.name}!', end="")
        print(' 💥HEADSHOT!') if headshot else print();

        damage = (self.damage * 2) if headshot else self.damage
        damage = max(damage - enemy.armor // 2, 1)
        enemy.hp = max(0, enemy.hp - damage)

        print(f'У {enemy.name} осталось ❤️ {enemy.hp} hp')            

def createPlayer():
    имя, hp, armor, damage = input().split()
    return Player(имя, int(hp), int(armor), int(damage))    

def fight( shooter, victim ):
    shooter.attack(victim)
    if victim.hp == 0:
        print(f'Победил {shooter.name}')
    return not (victim.hp == 0)


shooter = createPlayer()
victim = createPlayer()
while fight(shooter, victim):
    shooter, victim = victim, shooter
