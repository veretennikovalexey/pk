class Label:
    ''' UI-система. Часть 2 '''
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

class Window:
    def __init__(self, title):
        self.title = title
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def show(self):
        print(f'Окно "{self.title}"')

        for element in self.elements:
            element.display()


icon_play = Icon("▶️")
btn_play = Button("Играть", icon_play)
label = Label("Выберите уровень:")
window = Window("Главное меню")

window.add_element(label)
window.add_element(btn_play)
window.show()            