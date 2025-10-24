import tkinter as tk

# Настройки
GRID_SIZE = 16
GRID_COUNT = 32

# Создание окна
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

# Главный цикл
root.mainloop()