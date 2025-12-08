class DamageEffect:
    def __init__(self, amount):
        self.amount = amount

    def apply(self, target):
        print(f'{target} получает {self.amount} урона')


class VisualEffect:
    def __init__(self, name):
        self.name = name

    def apply(self, target):
        print(f'Визуальный эффект: {self.name}')


class SoundEffect:
    def __init__(self, name):
        self.name = name

    def apply(self, target):
        print(f'Звук: {self.name}')


class Spell:
    '''ВЖУХ'''
    def __init__(self, name, damage=None, visual=None, sound=None):
        self.name = name
        self.damage = damage
        self.visual = visual
        self.sound = sound
        
    def cast(self, target):
        print(f'Кастуем {self.name} на {target}!')
        
        self.damage.apply(target)
        self.visual.apply(target)
        self.sound.apply(target)


'''
Людмила Колесникова

применяет эффекты, если они заданы

    def cast(self, target):
        print(f"Кастуем {self.name} на {target}!")
        if self.damage:
            self.damage.apply(target)
        if self.visual:
            self.visual.apply(target)
        if self.sound:
            self.sound.apply(target)
          

'''