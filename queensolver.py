import pprint
def canPlace(chessboard,pos_x,pos_y,n):
    '''pos_x is row position and pos_y is col position'''
    '''check whether it is safe place for placing queen'''
    '''firstly check for given column on the top'''
    for row in range(pos_x):
        if(chessboard[row][pos_y]=='Q'):
            return False
        
    row = pos_x
    col = pos_y
    '''check for top left diagonals'''
    while(row>=0 and col>=0):
        if chessboard[row][col]=='Q':
            return False
        row -=1
        col -=1
    '''check for top right diagonals'''
    row = pos_x
    col = pos_y
    
    while(row>=0 and col<n):
        if chessboard[row][col]=='Q':
            return False
        row -=1
        col +=1
        
    '''finally if all above checks passes return True'''
    return True
def solveNqueens(board,x,n):
    '''if we have successfully placed n queens return True'''
    if(x>=n):
        return True
    #iterate through columns for each row
    for col in range(n):
    #if the particular position is safe then place that queen
        if(canPlace(board,x,col,n)):
            board[x][col]='Q'
        #if the next queen can not be placed then backtrack
            if(solveNqueens(board,x+1,n)):
                return True
            '''back tracking'''
            board[x][col]=' '
    return False
n=int(input("Enter number of Q: "))
board=[[' ']*n for i in range(n)]
if(solveNqueens(board,0,n)):
    pprint.pprint(board)
else:
 print("No Solution")