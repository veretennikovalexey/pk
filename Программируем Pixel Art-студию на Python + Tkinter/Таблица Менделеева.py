import tkinter as tk

WIDTH, HEIGHT = 1200, 600
COLS, ROWS = 18, 10
EXTRA = 1
M = 6

cell_w = (WIDTH - M * (COLS + EXTRA + 1)) // (COLS + EXTRA)
cell_h = (HEIGHT - M * (ROWS + EXTRA + 1)) // (ROWS + EXTRA)

COLORS = {
    "alkali": "#ffc8c8",
    "noble": "#c8ffff",
    "empty": "#f0f0f0"
}

elements = {
    (2, 1): {"Z": 1, "s": "H",  "t": "alkali"},
    (2,18): {"Z": 2, "s": "He", "t": "noble"},
}

roman = ["I","II","III","IV","V","VI","VII"]

root = tk.Tk()
root.title("Таблица Менделеева")
c = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#f5f5fa")
c.pack()

for r in range(ROWS + EXTRA):
    for col in range(COLS + EXTRA):
        x = M + col * (cell_w + M)
        y = M + r * (cell_h + M)

        if r == 0 and col > 0:
            c.create_text(x+cell_w/2, y+cell_h/2, text=str(col))
            continue

        if col == 0 and 1 <= r <= 7:
            c.create_text(x+cell_w/2, y+cell_h/2, text=roman[r-1])
            continue

        data = elements.get((r, col))
        color = COLORS[data["t"]] if data else COLORS["empty"]

        c.create_rectangle(x, y, x+cell_w, y+cell_h, fill=color, outline="#999")

        if data:
            c.create_text(x+cell_w/2, y+cell_h/2, text=data["s"], font=("Verdana", 20))
            c.create_text(x+4, y+4, text=data["Z"], anchor="nw", font=("Verdana", 8))

root.mainloop()
