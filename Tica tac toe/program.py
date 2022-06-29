from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import time
import random

window = Tk()
window.title("Tic-Tac-Toe")
window.geometry('500x700')
window.maxsize(500, 700)
window.minsize(500, 700)
bg = ImageTk.PhotoImage(Image.open("p/Menu.png"))
X_pic = ImageTk.PhotoImage(Image.open('p/X.png'))
O_pic = ImageTk.PhotoImage(Image.open('p/O.png'))
player_pic = ImageTk.PhotoImage(Image.open('p/playervsplayer.png'))
pvsc_pic = ImageTk.PhotoImage(Image.open('p/playervscomputer.png'))
cvsc_pic = ImageTk.PhotoImage(Image.open('p/computervscomputer.png'))
exit_pic = ImageTk.PhotoImage(Image.open('p/exit.png'))
wojtek = ImageTk.PhotoImage(Image.open('p/wojte.png'))
Oturn = ImageTk.PhotoImage(Image.open('p/Oturn.png'))
Xturn = ImageTk.PhotoImage(Image.open('p/Xturn.png'))
resetpic = ImageTk.PhotoImage(Image.open('p/reset.png'))
returnpic = ImageTk.PhotoImage(Image.open('p/return.png'))
owin = ImageTk.PhotoImage(Image.open('p/Owin.png'))
xwin = ImageTk.PhotoImage(Image.open('p/Xwin.png'))
draw = ImageTk.PhotoImage(Image.open('p/draw.png'))
ce = ImageTk.PhotoImage(Image.open('p/ce.png'))
easy = ImageTk.PhotoImage(Image.open("p/easy.png"))
normal = ImageTk.PhotoImage(Image.open('p/normal.png'))
hard = ImageTk.PhotoImage(Image.open('p/hard.png'))
piotrek = ImageTk.PhotoImage(Image.open('p/piotrek.png'))
ja = ImageTk.PhotoImage(Image.open('p/ja.png'))
asia = ImageTk.PhotoImage(Image.open('p/asia.png'))


witch_player = 0
player = ['O', 'X']
tura = 1


def clean():
    for widget in window.winfo_children():
        widget.destroy()


def show_player(i):
    if i == 0:
        pic = piotrek
    elif i == 1:
        pic = asia
    elif i == 2:
        pic = ja  # ja
    elif i == 3 or i == 4:
        pic = wojtek
    return pic


def wpisywanie(r, c, i):
    if r == 0.28 and c == 0.32:
        buttons[0] = player[i]
    elif r == 0.5 and c == 0.32:
        buttons[1] = player[i]
    elif r == 0.72 and c == 0.32:
        buttons[2] = player[i]
    elif r == 0.28 and c == 0.5:
        buttons[3] = player[i]
    elif r == 0.5 and c == 0.5:
        buttons[4] = player[i]
    elif r == 0.72 and c == 0.5:
        buttons[5] = player[i]
    elif r == 0.28 and c == 0.68:
        buttons[6] = player[i]
    elif r == 0.5 and c == 0.68:
        buttons[7] = player[i]
    elif r == 0.72 and c == 0.68:
        buttons[8] = player[i]


def konwert_buttons_to_clik(x):
    if x == 0:
        return(0.28, 0.32)
    elif x == 1:
        return(0.5, 0.32)
    elif x == 2:
        return(0.72, 0.32)
    elif x == 3:
        return(0.28, 0.5)
    elif x == 4:
        return(0.5, 0.5)
    elif x == 5:
        return(0.72, 0.5)
    elif x == 6:
        return(0.28, 0.68)
    elif x == 7:
        return(0.5, 0.68)
    elif x == 8:
        return(0.72, 0.68)


def Win(Player):
    clean()
    global tura
    if witch_player == 3 or witch_player == 2:
        if player == 1:
            turn = owin
        else:
            turn = xwin

    else:
        if player == 1:
            turn = xwin
        else:
            turn = owin

    l = Label(window, image=bg)
    l.place(x=0, y=0, relwidth=1, relheigh=1)
    if Player == 10:
        l = Label(window, image=draw, font=('console', 20), justify=CENTER)
        l.pack()
    else:
        l = Label(window, image=turn,
                  font=('console', 20))
        l.pack()
    b = Button(image=resetpic, padx=50, pady=20,
               justify=CENTER, command=menu)
    b.pack()
    return 1


def chek_win(i):
    # Horizontal winning condition
    if(buttons[0] == buttons[1] and buttons[1] == buttons[2] and buttons[1] != 0):
        return Win(i)
    elif(buttons[3] == buttons[4] and buttons[4] == buttons[5] and buttons[4] != 0):
        return Win(i)
    elif(buttons[6] == buttons[7] and buttons[8] == buttons[7] and buttons[7] != 0):
        return Win(i)
    # Vertical Winning Condition
    elif(buttons[0] == buttons[3] and buttons[3] == buttons[6] and buttons[0] != 0):
        return Win(i)
    elif(buttons[1] == buttons[4] and buttons[4] == buttons[7] and buttons[1] != 0):
        return Win(i)
    elif(buttons[2] == buttons[5] and buttons[5] == buttons[8] and buttons[2] != 0):
        return Win(i)
    # Diagonal Winning Condition
    elif(buttons[0] == buttons[4] and buttons[4] == buttons[8] and buttons[4] != 0):
        return Win(i)
    elif(buttons[2] == buttons[4] and buttons[4] == buttons[6] and buttons[4] != 0):
        return Win(i)
    # Match Tie or Draw Condition
    elif tura == 9:
        return Win(10)
        # Game=Draw
    else:
        return 2


def clik_action(r, c):
    global tura
    if tura % 2 == 0:
        i = 0
        pic = O_pic
        turn = Xturn
    else:
        i = 1
        pic = X_pic
        turn = Oturn
    l = Label(window, image=(turn),
              font=('consolas', 20))
    l.pack()
    l.place(relx=0.5, rely=0, anchor=N)
    if witch_player == 3 and tura == 1:
        r = 0.72
        c = 0.68
    elif witch_player == 4:
        window.after(1000, pick_computer_normal)
    b = Button(image=pic, text=player[i], padx=45, pady=50)
    b.configure(image=pic)
    b.pack()
    b.place(relx=r, rely=c, anchor=CENTER)
    tura += 1
    wpisywanie(r, c, i)
    x = chek_win(i)
    if x != 1:
        if witch_player == 1 and tura % 2 != 0 and tura < 10:
            window.after(1000, pick_computer_easy)
        elif witch_player == 2 and tura % 2 != 0 and tura < 10:
            window.after(1000, pick_computer_normal)
        if witch_player == 3 and tura % 2 != 0 and tura < 10:
            window.after(1000, pick_computer_hard)


def button():
    buttons0 = Button(window, padx=50, pady=50,
                      command=lambda: clik_action(0.28, 0.32), background="#FF9900")
    buttons0.pack()
    buttons0.place(relx=0.28, rely=0.32, anchor=CENTER)
    buttons1 = Button(window, padx=50, pady=50,
                      command=lambda: clik_action(0.5, 0.32), background="#FF9900")
    buttons1.pack()
    buttons1.place(relx=0.5, rely=0.32, anchor=CENTER)
    buttons2 = Button(window, padx=50, pady=50, command=lambda: clik_action(
        0.72, 0.32), background="#FF9900")
    buttons2.pack()
    buttons2.place(relx=0.72, rely=0.32, anchor=CENTER)
    buttons3 = Button(window, padx=50, pady=50, command=lambda: clik_action(
        0.28, 0.5), background="#FF9900")
    buttons3.pack()
    buttons3.place(relx=0.28, rely=0.5, anchor=CENTER)
    buttons4 = Button(window, padx=50, pady=50,
                      command=lambda: clik_action(0.5, 0.5), background="#FF9900")
    buttons4.pack()
    buttons4.place(relx=0.5, rely=0.5, anchor=CENTER)
    buttons5 = Button(window, padx=50, pady=50,
                      command=lambda: clik_action(0.72, 0.5), background="#FF9900")
    buttons5.pack()
    buttons5.place(relx=0.72, rely=0.5, anchor=CENTER)
    buttons6 = Button(window, padx=50, pady=50, command=lambda: clik_action(
        0.28, 0.68), background="#FF9900")
    buttons6.pack()
    buttons6.place(relx=0.28, rely=0.68, anchor=CENTER)
    buttons7 = Button(window, padx=50, pady=50,
                      command=lambda: clik_action(0.5, 0.68), background="#FF9900")
    buttons7.pack()
    buttons7.place(relx=0.5, rely=0.68, anchor=CENTER)
    buttons8 = Button(window, padx=50, pady=50,
                      command=lambda: clik_action(0.72, 0.68), background="#FF9900")
    buttons8.pack()
    buttons8.place(relx=0.72, rely=0.68, anchor=CENTER)


def play():
    clean()
    l = Label(window, image=bg)
    l.place(x=0, y=0, relwidth=1, relheigh=1)
    m = Label(window, image=piotrek)
    m.pack()
    m.place(relx=0.23, rely=0, anchor=N)
    e = Label(window, image=show_player(witch_player))
    e.pack()
    e.place(relx=0.77, rely=0, anchor=N)
    l1 = Label(window, image=Oturn, font=('console', 20))
    l1.pack()
    button()
    if witch_player == 3:
        clik_action(5, 5)
    if witch_player == 4:
        clik_action(5, 5)


def menu():
    clean()
    global witch_player
    witch_player = 0

    l = Label(window, image=bg)
    l.place(x=0, y=0, relwidth=1, relheigh=1)
    global buttons
    buttons = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]
    global tura
    tura = 0

    button = Button(window, image=player_pic, padx=30,
                    pady=20, command=play)
    button.pack(padx=10, pady=20)
    button.place(relx=0.5, rely=0.2, anchor=CENTER)

    button1 = Button(window, image=pvsc_pic,
                     padx=25, pady=20, command=play_vs_ai)
    button1.pack(padx=10, pady=20)
    button1.place(relx=0.5, rely=0.4, anchor=CENTER)

    button2 = Button(window, image=cvsc_pic, padx=10,
                     pady=20, command=play_aivsai)
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
    l = Label(window, image=ce)
    l.pack()
    button = Button(window, image=easy, padx=45,
                    pady=20, command=play_easy)
    button.pack(padx=10, pady=20)
    button.place(relx=0.5, rely=0.2, anchor=CENTER)

    button1 = Button(window, image=normal, padx=35,
                     pady=20, command=play_normal)
    button1.pack(padx=10, pady=20)
    button1.place(relx=0.5, rely=0.4, anchor=CENTER)

    button2 = Button(window, image=hard, padx=43, pady=20, command=play_hard)
    button2.pack(padx=10, pady=20)
    button2.place(relx=0.5, rely=0.6, anchor=CENTER)
    button3 = Button(window, image=returnpic, padx=40,
                     pady=20, command=menu)
    button3.pack(padx=10, pady=20)
    button3.place(relx=0.5, rely=0.8, anchor=CENTER)


def play_easy():
    global witch_player
    witch_player = 1
    play()


def play_normal():
    global witch_player
    witch_player = 2
    play()


def play_hard():
    global witch_player
    witch_player = 3
    play()


def play_aivsai():
    global witch_player
    witch_player = 4
    play()


def pick_computer_hard():
    if tura == 3:
        if buttons[1] == 'O' or buttons[3] == 'O' or buttons[5] == 'O' or buttons[7] == 'O':
            clik_action(0.5, 0.5)
        elif buttons[2] == 'O' or buttons[6] == 'O':
            if buttons[2] == 'O':
                clik_action(0.28, 0.68)
            else:
                clik_action(0.72, 0.32)
        elif buttons[0] == 'O':
            clik_action(0.28, 0.68)
        elif buttons[4] == 'O':
            clik_action(0.28, 0.32)
        return 0
    if tura == 5:
        if buttons[0] == 'O' and buttons[4] == 'X' and buttons[8] == 'X' and buttons[5] != 'O':
            clik_action(0.72, 0.32)
        elif buttons[0] == 'O' and buttons[4] == 'X' and buttons[8] == 'X' and buttons[5]:
            clik_action(0.28, 0.68)
        elif buttons[2] == 'X' or buttons[6] == 'X' and buttons[0] == 0:
            clik_action(0.28, 0.32)
        elif buttons[0] == 'O':
            if buttons[2] == 'X' or buttons[6] == 'X':
                if buttons[2] == 'X' and buttons[6] == 0:
                    clik_action(0.28, 0.68)
                elif buttons[2] == 0:
                    clik_action(0.72, 0.32)
                else:
                    pick_computer_normal()
        elif buttons[4] == 'O' and (buttons[2] == 'O' or buttons[6] == 'O'):
            if buttons[2] == 0 or buttons[6] == 0:
                if buttons[2] == 0 and buttons[2] == 0:
                    clik_action(0.72, 0.32)
                elif buttons[6] == 0:
                    clik_action(0.28, 0.68)
                else:
                    pick_computer_normal()
        else:
            pick_computer_normal()
        return 0

    else:
        if tura != 0:
            pick_computer_normal()


def pick_computer_normal():
    for i in ['X', 'O']:
        counter = 0
        # poziomy
        for z in (0, 3, 6):
            counter = 0
            for x in range(z, z+3):
                if buttons[x] == i:
                    counter += 1

            if counter == 2:
                for x in range(z, z+3):
                    if buttons[x] == 0:
                        clik_action(konwert_buttons_to_clik(
                            x)[0], konwert_buttons_to_clik(x)[1])
                        return 0
        # piony
        counter = 0
        for z in range(3):
            counter = 0
            for x in (z, z+3, z+6):
                if buttons[x] == i:
                    counter += 1
            if counter == 2:
                for x in (z, z+3, z+6):
                    if buttons[x] == 0:
                        clik_action(konwert_buttons_to_clik(
                            x)[0], konwert_buttons_to_clik(x)[1])
                        return 0
        # skosy
        counter = 0
        for x in (0, 4, 8):
            if buttons[x] == i:
                counter += 1
        if counter == 2:
            for x in (0, 4, 8):
                if buttons[x] == 0:
                    clik_action(konwert_buttons_to_clik(
                        x)[0], konwert_buttons_to_clik(x)[1])
                    return 0
        counter = 0
        for x in (2, 4, 6):
            if buttons[x] == i:
                counter += 1
        if counter == 2:
            for x in (2, 4, 6):
                if buttons[x] == 0:
                    clik_action(konwert_buttons_to_clik(
                        x)[0], konwert_buttons_to_clik(x)[1])
                    return 0

        if counter < 2 and i == 'O':
            pick_computer_easy()
            return 0


def pick_computer_easy():

    while True:

        random_choice = random.randint(0, 8)

        if random_choice == 0 and buttons[0] == 0:
            clik_action(0.28, 0.32)
            break
        elif random_choice == 1 and buttons[1] == 0:
            clik_action(0.5, 0.32)
            break
        elif random_choice == 2 and buttons[2] == 0:
            clik_action(0.72, 0.32)
            break
        elif random_choice == 3 and buttons[3] == 0:
            clik_action(0.28, 0.5)
            break
        elif random_choice == 4 and buttons[4] == 0:
            clik_action(0.5, 0.5)
            break
        elif random_choice == 5 and buttons[5] == 0:
            clik_action(0.72, 0.5)
            break
        elif random_choice == 6 and buttons[6] == 0:
            clik_action(0.28, 0.68)
            break
        elif random_choice == 7 and buttons[7] == 0:
            clik_action(0.5, 0.68)
            break
        elif random_choice == 8 and buttons[8] == 0:
            clik_action(0.72, 0.68)
            break


menu()
window.mainloop()
