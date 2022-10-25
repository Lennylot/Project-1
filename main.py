board = [[0,0,0],
         [0,0,0],
         [0,0,0]]


def user_input():
    row_choice = int(input("Enter a number to choose row(0-2): "))          
    column_choice = int(input("Enter a number to choose column(0-2): "))
    return row_choice,column_choice

def player_move():
    player = 1
    row_choice,column_choice = user_input()
    board[row_choice][column_choice] = player
    return board
    


def display_board():
    for view in board:
        print(view)


def win_condition():
    #horizontal
    for rows in board:
        if rows.count(rows[0]) == len(rows) and rows[0] != 0:
            print(f"Player {rows[0]} is the winner by horizontal ")

    #vertical
    check_vertical_win = []
    for i in range(len(board)):
        for x in board:
            check_vertical_win.append(x[i])
        if check_vertical_win.count(check_vertical_win[0]) == len(check_vertical_win) and check_vertical_win[0] != 0:
            print(f"Player {rows[0]} is the winner by vertical ")

    #diagonal
    check_diagonal_win = []
    for d in range(len(board)):
        check_diagonal_win.append(board[d][d])
    if check_diagonal_win.count(check_diagonal_win[0]) == len(check_diagonal_win) and check_diagonal_win[0] != 0:
            print(f"Player {rows[0]} is the winner by \ ")

    #reverse diagonal
    reversed_cols = list(reversed(range(len(board))))
    reversed_rows = range(len(board))
    check_reversed_diagonal_win = []
    for reversed_cols,reversed_rows, in zip(reversed_cols,reversed_rows):
        check_reversed_diagonal_win.append(board[reversed_cols][reversed_rows])
    if check_reversed_diagonal_win.count(check_reversed_diagonal_win[0]) == len(check_reversed_diagonal_win) and check_reversed_diagonal_win[0] != 0:
            print(f"Player {rows[0]} is the winner by / ")




player_move()
display_board()
win_condition()



























