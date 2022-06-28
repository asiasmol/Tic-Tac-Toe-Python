from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
buttons = [0, 0, 0,
           0, 0, 0,
           0, 0, 0]
player = ['O', 'X']
tura = 0
X_pic = ImageTk.PhotoImage(Image.open('X.png'))
O_pic = ImageTk.PhotoImage(Image.open('O.png'))


def wpisywanie(r, c, i):
    if r == 1 and c == 1:
        buttons[0] = player[i]
    elif r == 1 and c == 2:
        buttons[1] = player[i]
    elif r == 1 and c == 3:
        buttons[2] = player[i]
    elif r == 2 and c == 1:
        buttons[3] = player[i]
    elif r == 2 and c == 2:
        buttons[4] = player[i]
    elif r == 2 and c == 3:
        buttons[5] = player[i]
    elif r == 3 and c == 1:
        buttons[6] = player[i]
    elif r == 3 and c == 2:
        buttons[7] = player[i]
    elif r == 3 and c == 3:
        buttons[8] = player[i]


# --- functions ---


def on_click(widget, r, c):
    global tura
    if tura % 2 == 0:
        i = 0
        pic = O_pic
    else:
        i = 1
        pic = X_pic

    widget['image'] = pic
    wpisywanie(r, c, i)

# --- main ---


root = Tk()

for y in range(3):
    for x in range(3):
        button = tk.Button(root, padx=50, pady=50)
        button['command'] = lambda arg=button: on_click(arg, y, x)
        button.grid(row=y, column=x)

print(buttons)
root.mainloop()
