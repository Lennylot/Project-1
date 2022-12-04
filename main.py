import random
num_row = 6
num_col = 7
print("Welcome to my Connect 4 game")
print("The player is number 1 and the computer is number 2")


board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]












def display_board():
    print("   0  1  2  3  4  5  6  ")
    for count, row in enumerate(board):
        print(count,row)


def stacking(col, player):
    col=col-1
    for rows in range(num_row-1,-1,-1):
        if board[rows][col] == 0:
            print("legal move")
            board[rows][col] = player
            break

def horizwin():
    for row in range(0,num_row):
        for col in range(0,4):
            if board[row][col] > 0:
             if board[row][col] == board[row][col+1] == \
                board[row][col+2] == board[row][col+3]:
                print("Player", board[row][col], "won!")
                return True

def vertwin():
    for row in range(0, 3):
        for col in range(0, num_col):
            if board[row][col] > 0:
                if board[row][col] == board[row+1][col] == \
                board[row+2][col] == board[row+3][col]:
                    print("Player", board[row][col], "won!")
                    return True

def diagwin():
    #this is going up and to the right
    for row in range(0,2):
        for col in range(0,7):
            if board[row][col] > 0:
                if board[row][col] == board[row-1][col+1] == \
                    board[row-2][col+2] == board[row-3][col+3]:
                    print("Player",board[row][col], "won!")
                    return True

    #going down and to the right
    for row in range(0,3):
        for col in range(0,4):
            if board[row][col] > 0:
                if board[row][col] == board[row+1][col+1] == \
                    board[row + 2][col + 2] == board[row + 3][col + 3]:
                    print("Player",board[row][col], "won!")
                    return True

def win():
    if horizwin() or vertwin() or diagwin():
        return True
    return False


def cpu_move(col,cpu_piece):
    col = col - 1
    for rows in range(num_row - 1, -1, -1):
        if board[rows][col] == 0:
            print("legal move")
            board[rows][col] = cpu_piece
            break


player = 1
cpu_piece = 2
while not win():
    col = int(input("Enter a column: "))
    stacking(col, player)
    random_column = random.randint(0, 6)
    cpu_move(random_column, cpu_piece)
    display_board()
















