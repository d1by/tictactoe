import random

def resetBoard():
    board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    return board

def drawBoard(board):
    for i in range(3):
        for j in range(3):
            print("| ", end="")
            print(board[i][j], end="")
            print(" ", end="")
        print("|",end="")
        if(i!=2):
            print("\n|---|---|---|")
        else:
            print("\n")
    return board

def playerMove(board):
    repeat = True
    while(repeat):
        row = int(input("Choose row (1-3): "))-1
        col = int(input("Choose column (1-3): "))-1
        if(row>2 or row<0 or col>2 or col<0):
            print("Invalid input!\n")
            continue
        elif(board[row][col]==" "):
            board[row][col] = "x"
            return board
        else:
            print("Spot already taken!\n")

def computerMove(board):
    repeat = True
    while(repeat):
        row = random.randint(0,2)
        col = random.randint(0,2)
        if(board[row][col]==" "):
            board[row][col] = "o"
            return board
        else:
            continue

def checkWinner(board):
    #checking rows
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][0] == board[i][2]):
            return board[i][0]
    #checking columns
    for i in range(3):
        if(board[0][i] == board[1][i] and board[0][i] == board[2][i]):
            return board[0][i]
    #checking diagonals
    if(board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        return board[0][0]
    elif(board[0][2]) == board[1][1] and board[0][2] == board[2][0]:
        return  board[0][2]
    
    return " "

spaces = 9
board = resetBoard()
board = drawBoard(board)

while(spaces>0 or winner==" "): 
    board = playerMove(board)
    spaces-=1
    drawBoard(board)
    winner = checkWinner(board)
    if(winner!=" " or spaces==0):
        break
    
    board = computerMove(board)
    spaces-=1
    drawBoard(board)
    winner = checkWinner(board)
    if(winner!=" " or spaces==0):
        break

if(winner == "x"):
    print("You won!")
elif(winner == "o"):
    print("You lost!")
else:
    print("Tied!")