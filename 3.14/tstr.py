from string.templatelib import Template, Interpolation

def render(template: Template) -> str:
    parts = []
    for item in template:
        if isinstance(item, str):
            parts.append(item)  # Это статическая текстовая часть
        elif isinstance(item, Interpolation):
            # Это интерполированное значение, преобразуем его в строку
            parts.append(str(item.value))
    return "".join(parts)

# Ваша программа будет выглядеть так:
# подключаем стороннюю библиотеку для рендера
from string.templatelib import Template

# тут т-строка
name = "Мир"
template = t"Привет, {name}!"

# тут принт рендер т-строка
print(render(template))  # Вывод: Привет, Мир!