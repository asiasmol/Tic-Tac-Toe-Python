def konwert_board_to_clik(place_in_board):
    if place_in_board == 0:
        return(0.28, 0.32)
    elif place_in_board == 1:
        return(0.5, 0.32)
    elif place_in_board == 2:
        return(0.72, 0.32)
    elif place_in_board == 3:
        return(0.28, 0.5)
    elif place_in_board == 4:
        return(0.5, 0.5)
    elif place_in_board == 5:
        return(0.72, 0.5)
    elif place_in_board == 6:
        return(0.28, 0.68)
    elif place_in_board == 7:
        return(0.5, 0.68)
    elif place_in_board == 8:
        return(0.72, 0.68)

def read_to_board(buttons,player,row,column):
    if row == 0.28 and column == 0.32:
        buttons[0] = player
    elif row == 0.5 and column == 0.32:
        buttons[1] = player
    elif row == 0.72 and column == 0.32:
        buttons[2] = player
    elif row == 0.28 and column == 0.5:
        buttons[3] = player
    elif row == 0.5 and column == 0.5:
        buttons[4] = player
    elif row == 0.72 and column == 0.5:
        buttons[5] = player
    elif row == 0.28 and column == 0.68:
        buttons[6] = player
    elif row == 0.5 and column == 0.68:
        buttons[7] = player
    elif row == 0.72 and column == 0.68:
        buttons[8] = player