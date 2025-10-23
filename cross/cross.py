import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Крестики-нолики")
# root.iconbitmap("icon.ico")  # Можно включить, если есть файл

current_player = "X"
buttons = []

def check_winner():
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a,b,c in combos:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            for i in (a,b,c):
                buttons[i].config(bg="lightgreen")
            return True
    return False

def empty_indices():
    return [i for i,b in enumerate(buttons) if b["text"] == ""]

def computer_move():
    free = empty_indices()
    if not free:
        return

    # 20% шанс сделать случайный ход
    if random.random() > 0.8:
        index = random.choice(free)
    else:
        # Попробовать выиграть
        index = find_best_move("O")
        if index is None:
            # Попробовать заблокировать X
            index = find_best_move("X")
        if index is None:
            index = random.choice(free)

    buttons[index]["text"] = "O"
    if check_winner():
        messagebox.showinfo("Победа!", "Компьютер выиграл!")
    elif all(b["text"] != "" for b in buttons):
        messagebox.showinfo("Ничья!", "Ничья!")

def find_best_move(player):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a,b,c in combos:
        line = [buttons[a]["text"], buttons[b]["text"], buttons[c]["text"]]
        if line.count(player) == 2 and line.count("") == 1:
            return [a,b,c][line.index("")]
    return None

def on_click(index):
    global current_player
    if buttons[index]["text"] == "" and current_player == "X":
        buttons[index]["text"] = "X"
        if check_winner():
            messagebox.showinfo("Победа!", "Ты выиграл!")
            return
        elif all(b["text"] != "" for b in buttons):
            messagebox.showinfo("Ничья!", "Ничья!")
            return
        current_player = "O"
        root.after(400, computer_turn)

def computer_turn():
    global current_player
    computer_move()
    current_player = "X"

def reset_game():
    global current_player
    for b in buttons:
        b.config(text="", bg="SystemButtonFace")
    current_player = "X" if random.random() < 0.5 else "O"
    if current_player == "O":
        root.after(500, computer_turn)

for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 30), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_button = tk.Button(root, text="Новая игра", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

reset_game()
root.mainloop()
