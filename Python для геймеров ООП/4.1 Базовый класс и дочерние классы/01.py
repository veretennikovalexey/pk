# Пример 1: Создаем базовый класс

class Hero:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def show(self):
        print(f'{self.name}: {self.hp} HP')        

# Пример 2: Создаем дочерние классы

class Elf( Hero ):
    def apply_bonus(self):
        self.hp += 10

class Orc( Hero ):
    def apply_bonus(self):
        self.hp += 30

elf = Elf("Legolas")
orc = Orc("Grom")

elf.apply_bonus()
elf.show()

orc.apply_bonus()
orc.show()                

''' error
class Hero:
  def __init__(self, name):
    self.name = name

class Fighter(Hero):
  print(self.name)
'''

class Hero:
    def __init__(self, name):
        self.name = name

class Fighter(Hero):
    def show_name(self):
        print(self.name)

karate_pacan = Fighter("Karate pacan")
karate_pacan.show_name()