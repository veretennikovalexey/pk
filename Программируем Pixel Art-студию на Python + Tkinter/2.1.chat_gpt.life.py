import tkinter as tk

# Настройки
GRID_SIZE = 16
GRID_COUNT = 50
cells = {}
draw_color = "black"
running = False  # флаг работы игры

# Создание главного окна
root = tk.Tk()
root.title("Pixel Art Studio")
root.resizable(False, False)

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

# Рисование мышкой
def draw(event):
    paint(event, draw_color)

# Отрисовка сетки
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

# Правила игры "Жизнь"
def step():
    global running
    if not running:
        return

    new_state = {}
    for x in range(GRID_COUNT):
        for y in range(GRID_COUNT):
            # считаем соседей
            neighbors = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < GRID_COUNT and 0 <= ny < GRID_COUNT
                            and cells.get((nx, ny)) == "black"):
                        neighbors += 1

            # применяем правила
            if cells[(x, y)] == "black":
                if neighbors in (2, 3):
                    new_state[(x, y)] = "black"
                else:
                    new_state[(x, y)] = "white"
            else:
                if neighbors == 3:
                    new_state[(x, y)] = "black"
                else:
                    new_state[(x, y)] = "white"

    # обновляем отображение
    for (x, y), color in new_state.items():
        canvas.itemconfig(f"cell_{x}_{y}", fill=color)
    cells.update(new_state)

    root.after(200, step)  # шаг каждые 200 мс

# Кнопка запуска
def start_life():
    global running
    running = not running
    if running:
        start_button.config(text="Stop")
        step()
    else:
        start_button.config(text="Start")

# Привязка событий
draw_grid()
canvas.bind("<Button-1>", draw)
canvas.bind("<B1-Motion>", draw)

start_button = tk.Button(root, text="Start", command=start_life)
start_button.pack(pady=5)

root.mainloop()
