from PIL import ImageTk, Image

background_pic = ImageTk.PhotoImage(Image.open("p/Menu.png"))
X_pic = ImageTk.PhotoImage(Image.open('p/X.png'))
O_pic = ImageTk.PhotoImage(Image.open('p/O.png'))
player_vs_player_pic = ImageTk.PhotoImage(Image.open('p/playervsplayer.png'))
p_vs_ai_pic = ImageTk.PhotoImage(Image.open('p/playervscomputer.png'))
ai_vs_ai_pic = ImageTk.PhotoImage(Image.open('p/computervscomputer.png'))
exit_pic = ImageTk.PhotoImage(Image.open('p/exit.png'))
wojtek = ImageTk.PhotoImage(Image.open('p/wojte.png'))
Oturn = ImageTk.PhotoImage(Image.open('p/Oturn.png'))
Xturn = ImageTk.PhotoImage(Image.open('p/Xturn.png'))
resetpic = ImageTk.PhotoImage(Image.open('p/reset.png'))
returnpic = ImageTk.PhotoImage(Image.open('p/return.png'))
owin = ImageTk.PhotoImage(Image.open('p/Owin.png'))
xwin = ImageTk.PhotoImage(Image.open('p/Xwin.png'))
draw = ImageTk.PhotoImage(Image.open('p/draw.png'))
choose_enemy = ImageTk.PhotoImage(Image.open('p/ce.png'))
easy = ImageTk.PhotoImage(Image.open("p/easy.png"))
normal = ImageTk.PhotoImage(Image.open('p/normal.png'))
hard = ImageTk.PhotoImage(Image.open('p/hard.png'))
piotrek = ImageTk.PhotoImage(Image.open('p/piotrek.png'))
ja = ImageTk.PhotoImage(Image.open('p/ja.png'))
asia = ImageTk.PhotoImage(Image.open('p/asia.png'))
computer_game_pic = ImageTk.PhotoImage(Image.open('p/computergame.png'))
playerone = ImageTk.PhotoImage(Image.open('p/playerone.png'))
playertwo = ImageTk.PhotoImage(Image.open('p/playertwo.png'))


def show_player(which_play):
    if which_play == 0:
        pic = piotrek
    elif which_play == 1:
        pic = asia
    elif which_play == 2:
        pic = ja  # ja
    elif which_play == 3 or which_play == 4:
        pic = wojtek
    return pic
