class Label:
    ''' UI-система. Часть 1 '''
    def __init__(self, text):
        self.text = text

    def display(self):
        print(f'Надпись: {self.text}')

class Icon:
    def __init__(self, name):
        self.name  = name 

    def show(self):
        print(f'Иконка: {self.name}')

class Button:
    def __init__(self, text, icon=None):
        self.text = text
        self.icon = icon

    def display(self):
        print(f'[{self.text}]')

        if self.icon:
            self.icon.show()
