class ChocoChip:
    def use(self):
        print('Добавляем шоколадную крошку')


class NutSprinkles:
    def use(self):    
        print('Добавляем орешки')
        super().use()


class Cookie(NutSprinkles, ChocoChip):
    def use(self):    
        print('Формируем печеньку')
        super().use()