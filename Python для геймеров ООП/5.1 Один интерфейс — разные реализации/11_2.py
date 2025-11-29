# Людмила Колесникова

class Weapon:
    def interact(self):
        print('Вы атаковали врага!')


class Potion:
    def interact(self):
        print('Вы восстановили здоровье!')


class Pet:
    def interact(self):
        print('Питомец радуется!')


class Chest:
    def interact(self):
        print('Вы открыли сундук и нашли золото!')


class Trap:
    def interact(self):
        print('О нет! Вы попали в ловушку!')


def interact_with_all(objects):
    for _ in objects:
        _.interact()


n = int(input())    
objects = []

for _ in range(n):
    name = input()
    if name == "Weapon":
      objects.append(Weapon())  
    elif name == "Potion":
      objects.append(Potion())  
    elif name == "Pet":
      objects.append(Pet())  
    elif name == "Chest":
      objects.append(Chest())  
    elif name == "Trap":
      objects.append(Trap())       

interact_with_all(objects)