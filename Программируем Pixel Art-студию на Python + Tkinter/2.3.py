import tkinter as tk

# Настройки
GRID_SIZE = 16
GRID_COUNT = 32
cells = {}
draw_color = "black"
eraser_color = "white"
fill_color = "red"

# Создание главного окна
root = tk.Tk()
root.title("Pixel Art Studio")
root.resizable(False, False)

# Создание холста
canvas = tk.Canvas(
    root,
    width=GRID_SIZE * GRID_COUNT,
    height=GRID_SIZE * GRID_COUNT,
    bg="white"
)
canvas.pack()

# Функция для закрашивания клетки
def paint(event, color):
    x = event.x // GRID_SIZE
    y = event.y // GRID_SIZE

    if 0 <= x < GRID_COUNT and 0 <= y < GRID_COUNT:
        canvas.itemconfig(f"cell_{x}_{y}", fill=color)
        cells[(x, y)] = color

# Функция рисования карандашом
def draw(event):
    paint(event, draw_color)
	
# Функция ластика
def erase(event):
    paint(event, eraser_color)
	
# Функция заливки фона
def fill_background():
    global eraser_color
    for (x, y), color in cells.items():
        if color == "white":
            canvas.itemconfig(f"cell_{x}_{y}", fill=fill_color)
            cells[(x, y)] = fill_color
    eraser_color = fill_color

# Функция отрисовки сетки
def draw_grid():
    for x in range(GRID_COUNT):
        for y in range(GRID_COUNT):
            x1 = x * GRID_SIZE
            y1 = y * GRID_SIZE
            x2 = x1 + GRID_SIZE
            y2 = y1 + GRID_SIZE
            
            canvas.create_rectangle(
                x1, y1, x2, y2,
                outline="lightgray",
                fill="white",
                tags=f"cell_{x}_{y}"
            )

            cells[(x, y)] = "white"
			
draw_grid()

# Привязка событий левой кнопки мыши
canvas.bind("<Button-1>", draw)
canvas.bind("<B1-Motion>", draw)

# Привязка событий правой кнопки мыши
canvas.bind("<Button-3>", erase)
canvas.bind("<B3-Motion>", erase)

# Создаем панель инструментов
toolbar = tk.Frame(root)
toolbar.pack(pady=5)

# Кнопка заливки фона
fill_btn = tk.Button(toolbar, text="Заливка фона", command=fill_background)
fill_btn.pack(side=tk.LEFT, padx=5)

# Запуск главного цикла программы
root.mainloop()