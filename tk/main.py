import tkinter as tk
from table_data import table

root = tk.Tk()
root.title("")

FONT = ("Segoe UI", 16)

roman = ["I", "II", "III", "IV", "V", "VI", "VII"]

def cell_color(period, group):
    r = 40 + period * 25
    g = 60 + group * 7
    b = 180 - period * 15
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return f"#{r:02x}{g:02x}{b:02x}"

for col in range(1, 19):
    tk.Label(
        root,
        text=str(col),
        width=5,
        height=2,
        font=FONT,
        bg="#dddddd",
        relief="solid",
        borderwidth=2
    ).grid(row=0, column=col, padx=2, pady=2)

for row in range(1, 8):
    tk.Label(
        root,
        text=roman[row - 1],
        width=5,
        height=2,
        font=FONT,
        bg="#dddddd",
        relief="solid",
        borderwidth=2
    ).grid(row=row, column=0, padx=2, pady=2)

for row in range(len(table)):
    for col in range(len(table[row])):
        tk.Label(
            root,
            text=table[row][col],
            width=5,
            height=2,
            font=FONT,
            bg=cell_color(row + 1, col + 1),
            relief="solid",
            borderwidth=2
        ).grid(row=row + 1, column=col + 1, padx=2, pady=2)

root.mainloop()
