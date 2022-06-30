
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import time
import random
from functions1 import *


window = Tk()
window.title("Tic-Tac-Toe")
window.geometry('500x700')
window.maxsize(500, 700)
window.minsize(500, 700)

from imagine import *

which_play = 0
player = ['O', 'X']
tura = 1


def clean():
    for widget in window.winfo_children():
        widget.destroy()


def Win(which_player):
    clean()
    global tura
    if which_play != 0:
        if which_player != 1:
            win_pic = owin
        else:
            win_pic = xwin

    else:
        if which_player == 1:
            win_pic = xwin
        else:
            win_pic = owin

    background = Label(window, image=background_pic)
    background.place(x=0, y=0, relwidth=1, relheigh=1)
    if which_player == 10:
        draw_pic = Label(window, image=draw, font=(
            'console', 20), justify=CENTER)
        draw_pic.pack()
    else:
        win = Label(window, image=win_pic,
                    font=('console', 20))
        win.pack()
    restart_button = Button(image=resetpic, padx=50, pady=20,
                            justify=CENTER, command=menu)
    restart_button.pack()
    return True


def chek_win(which_player):
    # Horizontal winning condition
    if(board[0] == board[1] and board[1] == board[2] and board[1] != 0):
        return Win(which_player)
    elif(board[3] == board[4] and board[4] == board[5] and board[4] != 0):
        return Win(which_player)
    elif(board[6] == board[7] and board[8] == board[7] and board[7] != 0):
        return Win(which_player)
    # Vertical Winning Condition
    elif(board[0] == board[3] and board[3] == board[6] and board[0] != 0):
        return Win(which_player)
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != 0):
        return Win(which_player)
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != 0):
        return Win(which_player)
    # Diagonal Winning Condition
    elif(board[0] == board[4] and board[4] == board[8] and board[4] != 0):
        return Win(which_player)
    elif(board[2] == board[4] and board[4] == board[6] and board[4] != 0):
        return Win(which_player)
    # Match Tie or Draw Condition
    elif tura == 9 and (which_play == 2 or which_play == 1 or which_play == 0):
        return Win(10)
        # Game=Draw
    elif tura == 10:
        return Win(10)
    else:
        return False


def clik_action(row, column):
    global tura
    if tura % 2 == 0:
        which_player = 0
        X_or_O_pic = O_pic
        turn = Xturn
        if which_play == 0:
            turn = playertwo
    else:
        which_player = 1
        X_or_O_pic = X_pic
        turn = Oturn
        if which_play == 0:
            turn = playerone
    if which_play == 4:
        turn = computer_game_pic

    turn_pic = Label(window, image=(turn),
                     font=('consolas', 20))

    turn_pic.pack()
    turn_pic.place(relx=0.5, rely=0, anchor=N)
    if which_play == 3 and tura == 1:
        row = 0.72
        column = 0.68

    board_button = Button(
        image=X_or_O_pic, text=player[which_player], padx=45, pady=50)
    board_button.configure(image=X_or_O_pic)
    board_button.pack()
    board_button.place(relx=row, rely=column, anchor=CENTER)
    tura += 1
    read_to_board(board, player[which_player], row, column)
    win = chek_win(which_player)
    if win != True:
        if which_play == 1 and tura % 2 != 0 and tura < 10:
            window.after(1000, pick_computer_easy)
        elif which_play == 2 and tura % 2 != 0 and tura < 10:
            window.after(1000, pick_computer_normal)
        elif which_play == 3 and tura % 2 != 0 and tura <= 10:
            window.after(1000, pick_computer_hard)
        elif which_play == 4 and tura < 10:
            window.after(1000, pick_computer_normal)


def buttons():
    board0 = Button(window, padx=50, pady=50,
                    command=lambda: clik_action(0.28, 0.32), background="#FF9900")
    board0.pack()
    board0.place(relx=0.28, rely=0.32, anchor=CENTER)
    board1 = Button(window, padx=50, pady=50,
                    command=lambda: clik_action(0.5, 0.32), background="#FF9900")
    board1.pack()
    board1.place(relx=0.5, rely=0.32, anchor=CENTER)
    board2 = Button(window, padx=50, pady=50, command=lambda: clik_action(
        0.72, 0.32), background="#FF9900")
    board2.pack()
    board2.place(relx=0.72, rely=0.32, anchor=CENTER)
    board3 = Button(window, padx=50, pady=50, command=lambda: clik_action(
        0.28, 0.5), background="#FF9900")
    board3.pack()
    board3.place(relx=0.28, rely=0.5, anchor=CENTER)
    board4 = Button(window, padx=50, pady=50,
                    command=lambda: clik_action(0.5, 0.5), background="#FF9900")
    board4.pack()
    board4.place(relx=0.5, rely=0.5, anchor=CENTER)
    board5 = Button(window, padx=50, pady=50,
                    command=lambda: clik_action(0.72, 0.5), background="#FF9900")
    board5.pack()
    board5.place(relx=0.72, rely=0.5, anchor=CENTER)
    board6 = Button(window, padx=50, pady=50, command=lambda: clik_action(
        0.28, 0.68), background="#FF9900")
    board6.pack()
    board6.place(relx=0.28, rely=0.68, anchor=CENTER)
    board7 = Button(window, padx=50, pady=50,
                    command=lambda: clik_action(0.5, 0.68), background="#FF9900")
    board7.pack()
    board7.place(relx=0.5, rely=0.68, anchor=CENTER)
    board8 = Button(window, padx=50, pady=50,
                    command=lambda: clik_action(0.72, 0.68), background="#FF9900")
    board8.pack()
    board8.place(relx=0.72, rely=0.68, anchor=CENTER)


def play():
    clean()
    background = Label(window, image=background_pic)
    background.place(x=0, y=0, relwidth=1, relheigh=1)
    enemy_pic = Label(window, image=show_player(which_play))
    enemy_pic.pack()
    enemy_pic.place(relx=0.77, rely=0, anchor=N)
    our_pic = Label(window, image=piotrek)
    turn_pic = Label(window, image=Oturn, font=('console', 20))
    if which_play == 4:
        our_pic = Label(window, image=show_player(which_play))
        turn_pic = Label(window, image=computer_game_pic, font=('console', 20))
    if which_play == 0:
        turn_pic = Label(window, image=playerone, font=('console', 20))
    our_pic.pack()
    our_pic.place(relx=0.23, rely=0, anchor=N)
    turn_pic.pack()
    buttons()
    if which_play == 3:
        clik_action(5, 5)
    if which_play == 4:
        clik_action(5, 5)


def menu():
    clean()
    global which_play
    which_play = 0

    background = Label(window, image=background_pic)
    background.place(x=0, y=0, relwidth=1, relheigh=1)
    global board
    board = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]
    global tura
    tura = 0

    play_button = Button(window, image=player_vs_player_pic, padx=30,
                         pady=20, command=play)
    play_button.pack(padx=10, pady=20)
    play_button.place(relx=0.5, rely=0.2, anchor=CENTER)

    play_vs_ai_button = Button(window, image=p_vs_ai_pic,
                               padx=25, pady=20, command=menu_ai)
    play_vs_ai_button.pack(padx=10, pady=20)
    play_vs_ai_button.place(relx=0.5, rely=0.4, anchor=CENTER)

    play_ai_vs_ai_button = Button(window, image=ai_vs_ai_pic, padx=10,
                                  pady=20, command=play_ai_vs_ai)
    play_ai_vs_ai_button.pack()
    play_ai_vs_ai_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    exit_button = Button(window, image=exit_pic, padx=63,
                         pady=20, command=window.destroy)
    exit_button.pack(padx=10, pady=20)
    exit_button.place(relx=0.5, rely=0.8, anchor=CENTER)


def menu_ai():
    clean()
    background = Label(window, image=background_pic)
    background.place(x=0, y=0, relwidth=1, relheigh=1)
    label_choose_enemy = Label(window, image=choose_enemy)
    label_choose_enemy.pack()
    play_easy_button = Button(window, image=easy, padx=45,
                              pady=20, command=play_easy)
    play_easy_button.pack(padx=10, pady=20)
    play_easy_button.place(relx=0.5, rely=0.2, anchor=CENTER)

    play_noraml_button = Button(window, image=normal, padx=35,
                                pady=20, command=play_normal)
    play_noraml_button.pack(padx=10, pady=20)
    play_noraml_button.place(relx=0.5, rely=0.4, anchor=CENTER)

    play_hard_button = Button(
        window, image=hard, padx=43, pady=20, command=play_hard)
    play_hard_button.pack(padx=10, pady=20)
    play_hard_button.place(relx=0.5, rely=0.6, anchor=CENTER)
    return_button = Button(window, image=returnpic, padx=40,
                           pady=20, command=menu)
    return_button.pack(padx=10, pady=20)
    return_button.place(relx=0.5, rely=0.8, anchor=CENTER)


def play_easy():
    global which_play
    which_play = 1
    play()


def play_normal():
    global which_play
    which_play = 2
    play()


def play_hard():
    global which_play
    which_play = 3
    play()


def play_ai_vs_ai():
    global which_play
    which_play = 4
    play()


def pick_computer_hard():

    if tura == 3:
        if board[1] == 'O' or board[3] == 'O' or board[5] == 'O' or board[7] == 'O':
            clik_action(0.5, 0.5)
        elif board[2] == 'O' or board[6] == 'O':
            if board[2] == 'O':
                clik_action(0.28, 0.68)
            else:
                clik_action(0.72, 0.32)
        elif board[0] == 'O':
            clik_action(0.28, 0.68)
        elif board[4] == 'O':
            clik_action(0.28, 0.32)
        return 0
    elif tura == 5:
        if board[0] == 'O' and board[4] == 'X' and board[8] == 'X' and board[5] != 'O':
            clik_action(0.72, 0.32)
        elif board[0] == 'O' and board[4] == 'X' and board[8] == 'X' and board[5]:
            clik_action(0.28, 0.68)
        elif board[2] == 'X' or board[6] == 'X' and board[0] == 0:
            clik_action(0.28, 0.32)
        elif board[0] == 'O':
            if board[2] == 'X' or board[6] == 'X':
                if board[2] == 'X' and board[6] == 0:
                    clik_action(0.28, 0.68)
                elif board[2] == 0:
                    clik_action(0.72, 0.32)
                else:
                    pick_computer_normal()
        elif board[4] == 'O' and (board[2] == 'O' or board[6] == 'O'):
            if board[2] == 0 or board[6] == 0:
                if board[2] == 0 and board[2] == 0:
                    clik_action(0.72, 0.32)
                elif board[6] == 0:
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
    for player_symbol in ['X', 'O']:
        counter = 0
        # poziomy
        for horizontal_position in (0, 3, 6):
            counter = 0
            for place_in_horizontal_position in range(horizontal_position, horizontal_position+3):
                if board[place_in_horizontal_position] == player_symbol:
                    counter += 1

            if counter == 2:
                for place_in_horizontal_position in range(horizontal_position, horizontal_position+3):
                    if board[place_in_horizontal_position] == 0:
                        clik_action(konwert_board_to_clik(
                            place_in_horizontal_position)[0], konwert_board_to_clik(place_in_horizontal_position)[1])
                        return 0
        # piony
        counter = 0
        for vertical_position in range(3):
            counter = 0
            for place_in_vertical_position in (vertical_position, vertical_position+3, vertical_position+6):
                if board[place_in_vertical_position] == player_symbol:
                    counter += 1
            if counter == 2:
                for place_in_vertical_position in (vertical_position, vertical_position+3, vertical_position+6):
                    if board[place_in_vertical_position] == 0:
                        clik_action(konwert_board_to_clik(
                            place_in_vertical_position)[0], konwert_board_to_clik(place_in_vertical_position)[1])
                        return 0
        # skosy
        counter = 0
        for diagonal_position in (0, 4, 8):
            if board[diagonal_position] == player_symbol:
                counter += 1
        if counter == 2:
            for diagonal_position in (0, 4, 8):
                if board[diagonal_position] == 0:
                    clik_action(konwert_board_to_clik(
                        diagonal_position)[0], konwert_board_to_clik(diagonal_position)[1])
                    return 0
        counter = 0
        for diagonal_position in (2, 4, 6):
            if board[diagonal_position] == player_symbol:
                counter += 1
        if counter == 2:
            for diagonal_position in (2, 4, 6):
                if board[diagonal_position] == 0:
                    clik_action(konwert_board_to_clik(
                        diagonal_position)[0], konwert_board_to_clik(diagonal_position)[1])
                    return 0

        if counter < 2 and player_symbol == 'O':
            pick_computer_easy()
            return 0


def pick_computer_easy():
    while True:

        random_choice = random.randint(0, 8)

        if random_choice == 0 and board[0] == 0:
            clik_action(0.28, 0.32)
            break
        elif random_choice == 1 and board[1] == 0:
            clik_action(0.5, 0.32)
            break
        elif random_choice == 2 and board[2] == 0:
            clik_action(0.72, 0.32)
            break
        elif random_choice == 3 and board[3] == 0:
            clik_action(0.28, 0.5)
            break
        elif random_choice == 4 and board[4] == 0:
            clik_action(0.5, 0.5)
            break
        elif random_choice == 5 and board[5] == 0:
            clik_action(0.72, 0.5)
            break
        elif random_choice == 6 and board[6] == 0:
            clik_action(0.28, 0.68)
            break
        elif random_choice == 7 and board[7] == 0:
            clik_action(0.5, 0.68)
            break
        elif random_choice == 8 and board[8] == 0:
            clik_action(0.72, 0.68)
            break


menu()
window.mainloop()
