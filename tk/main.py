import tkinter as tk

from table_data import table

root = tk.Tk()
root.title("")

FONT = ("Segoe UI", 16)

for row in range(len(table)):
    for col in range(len(table[row])):
        text = table[row][col]

        cell = tk.Label(
            root,
            text=text,
            width=5,
            height=2,
            font=FONT,
            bg="white",
            relief="solid",
            borderwidth=2
        )

        cell.grid(row=row, column=col, padx=2, pady=2)

root.mainloop()
