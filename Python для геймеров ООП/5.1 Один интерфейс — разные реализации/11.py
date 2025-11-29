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
    objects.interact()

n = int(input())    

for _ in range(n):
    objects = eval(input())()
    interact_with_all(objects)