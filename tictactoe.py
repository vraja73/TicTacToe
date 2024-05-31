import random

def print_board(B):
    for i in B:
        print("\n")
        for j in i:
            if j == 0:
                print("[ ] ", end="")
            if j == 1:
                print("[X] ", end="")
            if j == 2:
                print("[O] ", end="")
def filled_board(A):
    return all(i == A[0] for i in A)

def check_win(A,B):
    
    if filled_board(A):
        return 10
    
    for i in range(3):
        if B[i][0] == B[i][1] == B[i][2] == 1:
            return 11
        
        if B[0][i] == B[1][i] == B[2][i] == 1:
            return 11
        
        if B[i][0] == B[i][1] == B[i][2] == 2:
            return 12
        
        if B[0][i] == B[1][i] == B[2][i] == 2:
            return 12

    if B[0][0] == B[1][1] == B[2][2] == 1:
        return 11

    if B[0][0] == B[1][1] == B[2][2] == 2:
        return 12         
    
    if B[0][2] == B[1][1] == B[2][0] == 1:
        return 11       

    if B[0][2] == B[1][1] == B[2][0] == 2:
        return 12       
    
    return 0

def valid_input(x):
    while True:
        if x <= 2 and x >=0:
            return x
        else:
            x = int(input("Invalid value. Please pick a number between 1-3\n"))-1

def is_square_filled(B):
    while True:
        row = int(input("\nChoose the row to place X (1-3) \n"))-1
        row = valid_input(row)
        col = int(input("\nChoose the column to place X (1-3) \n"))-1
        col = valid_input(col)
        
        if B[row][col] == 0:
            return [row,col]
        else:
            print("That square is already filled.\nPlease enter again.")

print("Welcome to TicTacToe")
board = [[0,0,0],[0,0,0],[0,0,0]]
filling_board = [[1,2,3],[4,5,6],[7,8,9]]

while True:
    print_board(board)

    [row,col] = is_square_filled(board)
    board[row][col] = 1  
    filling_board[row][col] = 0

    while True:
        c = random.choice([0,1,2])
        d = random.choice([0,1,2])
        if check_win(filling_board,board)>0:
            break
        if board[c][d] == 0:
            board[c][d] = 2
            filling_board[c][d] = 0
            break


    result = check_win(filling_board,board)
    if result > 0:
        print_board(board)
        print("\n")
        if result == 10:
            print("The game is a Tie")
        if result == 11:
            print("You Win!")
        if result == 12:
            print("Sorry You Lose")
        break
        


    
    
