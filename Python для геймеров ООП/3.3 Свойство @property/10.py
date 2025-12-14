class Hero:
    def __init__(self, level):
        self.__level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        if 1 <= value <= 80:
            self.__level = value
        else:
            print( 'Ошибка: уровень не может быть меньше 1, максимум 80.' )        