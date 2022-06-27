from ast import Lambda
from cProfile import label
from tkinter import *

window = Tk()
window.title("Tic-Tac-Toe")

player = ['O', 'X']
tura = 0

# def printlabel():
#     label1 =Label(window,text='kotek',padx=10,pady=10)
#     label1.pack()

# button=Button(window,text='coś',padx=20,pady=20,command=printlabel)
# button.pack()


def clean():
    for widget in window.winfo_children():
        widget.destroy()


def empty():
    label1 = Label(window, text="          ", padx=10, pady=5)
    label1.pack()


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


def chek_win():
    pass


def clik_action(r, c):
    global tura

    if tura % 2 == 0:
        i = 0
    else:
        i = 1
    Button(window, text=player[i], padx=45, pady=50).grid(row=r, column=c)
    tura += 1
    wpisywanie(r, c, i)

    print(buttons)


def button():
    buttons[0] = Button(window, padx=50, pady=50,
                        command=lambda: clik_action(1, 1)).grid(row=1, column=1)
    buttons[1] = Button(window, padx=50, pady=50,
                        command=lambda: clik_action(1, 2)).grid(row=1, column=2)
    buttons[2] = Button(window, padx=50, pady=50,
                        command=lambda: clik_action(1, 3)).grid(row=1, column=3)
    buttons[3] = Button(window, padx=50, pady=50,
                        command=lambda: clik_action(2, 1)).grid(row=2, column=1)
    buttons[4] = Button(window, padx=50, pady=50,
                        command=lambda: clik_action(2, 2)).grid(row=2, column=2)
    buttons[5] = Button(window, padx=50, pady=50,
                        command=lambda: clik_action(2, 3)).grid(row=2, column=3)
    buttons[6] = Button(window, padx=50, pady=50,
                        command=lambda: clik_action(3, 1)).grid(row=3, column=1)
    buttons[7] = Button(window, padx=50, pady=50,
                        command=lambda: clik_action(3, 2)).grid(row=3, column=2)
    buttons[8] = Button(window, padx=50, pady=50,
                        command=lambda: clik_action(3, 3)).grid(row=3, column=3)


def Player_vs_player():
    clean()
    Label(window, text='Turn', font=('console', 20)).grid(row=0, column=2)
    button()


def menu():
    global buttons
    buttons = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]
    empty()
    button = Button(window, text='Player vs PLayer', padx=30,
                    pady=20, command=Player_vs_player)
    button.pack()
    empty()
    button1 = Button(window, text='Play VS Computer', padx=25, pady=20)
    button1.pack()
    empty()
    button2 = Button(window, text='Computer VS Computer', padx=10, pady=20)
    button2.pack()
    empty()
    button4 = Button(window, text='Exit', padx=63,
                     pady=20, command=window.destroy)
    button4.pack()


menu()
window.mainloop()
