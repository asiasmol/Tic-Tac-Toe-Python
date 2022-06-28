from random import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random

window = Tk()
window.title("Tic-Tac-Toe")
window.geometry('400x500')
bg = ImageTk.PhotoImage(Image.open('Menu.png'))
X_pic = ImageTk.PhotoImage(Image.open('X.png'))
O_pic = ImageTk.PhotoImage(Image.open('O.png'))
player_pic = ImageTk.PhotoImage(Image.open('playervsplayer.png'))
pvsc_pic = ImageTk.PhotoImage(Image.open('playervscomputer.png'))
cvsc_pic = ImageTk.PhotoImage(Image.open('computervscomputer.png'))
exit_pic = ImageTk.PhotoImage(Image.open('exit.png'))
witch_player = 0
player = ['O', 'X']
tura = 0


def clean():
    for widget in window.winfo_children():
        widget.destroy()


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


def konwert_buttons_to_clik(x):
    if x == 0:
        return(1, 1)
    elif x == 1:
        return(1, 2)
    elif x == 2:
        return(1, 3)
    elif x == 3:
        return(2, 1)
    elif x == 4:
        return(2, 2)
    elif x == 5:
        return(2, 3)
    elif x == 6:
        return(3, 1)
    elif x == 7:
        return(3, 2)
    elif x == 8:
        return(3, 3)


def Win(Player):
    clean()
    if Player == 10:
        l = Label(window, text='Draw', font=('console', 20), justify=CENTER)
        l.pack()
    else:
        Label(window, text=(player[Player]+'Win'),
              font=('console', 20)).grid(row=0, column=2)
    b = Button(text='Reset', padx=50, pady=20, justify=CENTER, command=menu)
    b.pack()
    return 1


def chek_win(i):
    # Horizontal winning condition
    if(buttons[0] == buttons[1] and buttons[1] == buttons[2] and buttons[1] != None):
        return Win(i)
    elif(buttons[3] == buttons[4] and buttons[4] == buttons[5] and buttons[4] != None):
        return Win(i)
    elif(buttons[6] == buttons[7] and buttons[8] == buttons[7] and buttons[7] != None):
        return Win(i)
    # Vertical Winning Condition
    elif(buttons[0] == buttons[3] and buttons[3] == buttons[6] and buttons[0] != None):
        return Win(i)
    elif(buttons[1] == buttons[4] and buttons[4] == buttons[7] and buttons[1] != None):
        return Win(i)
    elif(buttons[2] == buttons[5] and buttons[5] == buttons[8] and buttons[2] != None):
        return Win(i)
    # Diagonal Winning Condition
    elif(buttons[0] == buttons[4] and buttons[4] == buttons[8] and buttons[4] != None):
        return Win(i)
    elif(buttons[2] == buttons[4] and buttons[4] == buttons[6] and buttons[4] != None):
        return Win(i)
    # Match Tie or Draw Condition
    elif tura == 9:
        return Win(10)
        # Game=Draw


def clik_action(r, c):
    global tura
    if tura % 2 == 0:
        i = 0
        pic = O_pic
    else:
        i = 1
        pic = X_pic

    Label(window, text=(player[i-1]+" Turn"),
          font=('consolas', 20)).grid(row=0, column=2)
    Button(image=pic, text=player[i], padx=45, pady=50).grid(row=r, column=c)
    tura += 1
    wpisywanie(r, c, i)
    x = chek_win(i)
    print(x)
    if x != 1:
        print(witch_player)

        if witch_player == 1 and tura % 2 != 0 and tura < 10:
            pick_computer_easy()
        elif witch_player == 2 and tura % 2 != 0 and tura < 10:
            pick_computer_normal()

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
    Label(window, text='O Turn', font=('console', 20)).grid(row=0, column=2)
    button()


def menu():
    clean()
    l = Label(window, image=bg)
    l.place(x=0, y=0, relwidth=1, relheigh=1)
    global buttons
    buttons = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]
    global tura
    tura = 0

    button = Button(window, image=player_pic, padx=30,
                    pady=20, command=Player_vs_player)
    button.pack(padx=10, pady=20)
    button.place(relx=0.5, rely=0.2, anchor=CENTER)

    button1 = Button(window, image=pvsc_pic,
                     padx=25, pady=20, command=play_vs_ai)
    button1.pack(padx=10, pady=20)
    button1.place(relx=0.5, rely=0.4, anchor=CENTER)

    button2 = Button(window, image=cvsc_pic, padx=10, pady=20)
    button2.pack()
    button2.place(relx=0.5, rely=0.6, anchor=CENTER)

    button3 = Button(window, image=exit_pic, padx=63,
                     pady=20, command=window.destroy)
    button3.pack(padx=10, pady=20)
    button3.place(relx=0.5, rely=0.8, anchor=CENTER)


def play_vs_ai():
    clean()
    l = Label(window, image=bg)
    l.place(x=0, y=0, relwidth=1, relheigh=1)
    button = Button(window, text='easy', padx=45,
                    pady=20, command=play_easy)
    button.pack(padx=10, pady=20)
    button.place(relx=0.5, rely=0.2, anchor=CENTER)

    button1 = Button(window, text='Normal', padx=35, pady=20)
    button1.pack(padx=10, pady=20)
    button1.place(relx=0.5, rely=0.4, anchor=CENTER)

    button2 = Button(window, text='Hard', padx=43, pady=20)
    button2.pack(padx=10, pady=20)
    button2.place(relx=0.5, rely=0.6, anchor=CENTER)
    button3 = Button(window, text='Return', padx=40,
                     pady=20, command=menu)
    button3.pack(padx=10, pady=20)
    button3.place(relx=0.5, rely=0.8, anchor=CENTER)


def play_easy():
    global witch_player
    witch_player = 1
    Player_vs_player()


def play_normal():
    global witch_player
    witch_player = 2
    Player_vs_player()


def pick_computer_normal():
    pass


def pick_computer_easy():
    print('kotek')
    while True:
        random_choice = random.randint(0, 8)
        print(random_choice)
        if random_choice == 0 and buttons[0] == None:
            clik_action(1, 1)
            break
        elif random_choice == 1 and buttons[1] == None:
            clik_action(1, 2)
            break
        elif random_choice == 2 and buttons[2] == None:
            clik_action(1, 3)
            break
        elif random_choice == 3 and buttons[3] == None:
            clik_action(2, 1)
            break
        elif random_choice == 4 and buttons[4] == None:
            clik_action(2, 2)
            break
        elif random_choice == 5 and buttons[5] == None:
            clik_action(2, 3)
            break
        elif random_choice == 6 and buttons[6] == None:
            clik_action(3, 1)
            break
        elif random_choice == 7 and buttons[7] == None:
            clik_action(3, 2)
            break
        elif random_choice == 8 and buttons[8] == None:
            clik_action(3, 3)
            break


menu()
window.mainloop()
