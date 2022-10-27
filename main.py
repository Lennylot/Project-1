import random

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def user_input():
    row_choice = int(input("Enter a number to choose row(0-2): "))
    column_choice = int(input("Enter a number to choose column(0-2): "))
    return row_choice, column_choice




def player_move():
    try:
        player_piece = 1
        row_choice, column_choice = user_input()
        board[row_choice][column_choice] = player_piece
    except:
        print("Make sure to input numbers from (0-2) because the game won't work")



def display_board():
    print("   0  1  2")
    for count, row in enumerate(board):
        print(count,row)


def win_condition():
    # horizontal
    for rows in board:
        if rows.count(rows[1]) == len(rows) and rows[2] != 0:
            print(f"Player {rows[0]} is the winner by horizontal ")
            return True
    # vertical
    check_vertical_win = []
    for i in range(len(board)):
        for x in board:
            check_vertical_win.append(x[i])
        if check_vertical_win.count(check_vertical_win[1]) == len(check_vertical_win) and check_vertical_win[2] != 0:
            print(f"Player {rows[0]} is the winner by vertical ")
            return True
    # diagonal
    check_diagonal_win = []
    for d in range(len(board)):
        check_diagonal_win.append(board[d][d])
    if check_diagonal_win.count(check_diagonal_win[1]) == len(check_diagonal_win) and check_diagonal_win[2] != 0:
        print(f"Player {rows[0]} is the winner by \ ")
        return True
    # reverse diagonal
    reversed_cols = list(reversed(range(len(board))))
    reversed_rows = range(len(board))
    check_reversed_diagonal_win = []
    for reversed_cols, reversed_rows, in zip(reversed_cols, reversed_rows):
        check_reversed_diagonal_win.append(board[reversed_cols][reversed_rows])
    if check_reversed_diagonal_win.count(check_reversed_diagonal_win[1]) == len(check_reversed_diagonal_win) and \
            check_reversed_diagonal_win[2] != 0:
        print(f"Player {rows[0]} is the winner by / ")
        return True

    return False

def cpu_move():
    cpu_piece = 2
    random_row = random.randint(0, 2)
    random_column = random.randint(0, 2)
    board[random_row][random_column] = cpu_piece








while True:
    display_board()
    player_move()
    cpu_move()
    if board == 1:
        cpu_move()
    if win_condition():

        display_board()
        break








