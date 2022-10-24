board = [[1,2,3],
         [4,5,6],
         [7,8,9]]



def player_move(game_board, player, row, column):
    
    game_board[row][column] = player
    return game_board
    


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




























