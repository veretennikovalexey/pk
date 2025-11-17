class Npc:
    def __init__(self, name, mood):
        self.__name = name
        self.__mood = mood

    def set_mood(self, value):
        if not 0 <= value <= 100:
            print('Ошибка: настроение должно быть от 0 до 100!')
        else:            
            self.__mood = value    

    def get_mood(self):
        return self.__mood