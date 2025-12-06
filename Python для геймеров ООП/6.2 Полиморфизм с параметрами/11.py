class Wand:
    def use(self, power, speed=1):
        print(f"Посох усиливает заклинание силой {power}, скорость {speed}")


'''
6.2 Полиморфизм с параметрами, шаг 11
Измените класс так, чтобы следующий код выполнялся без ошибок


def activate(item):
    item.use(10)

activate(Wand())        
'''