def is_valid_cross(board, idx, val):
    y,x = idx
    for i in range(9):
        if board[y][i] == val and i != x:
            return False
        if board[i][x] == val and i != y:
            return False
    return True
        

def is_valid_square(board, idx, val):
    casos = [[0,1,2],[-1,0,1,],[-2,-1,0]]
    y,x = idx
    casoy = casos[y%3]
    casox = casos[x%3]
    for j in casoy:
        for i in casox:
            if j != 0 or i != 0:
                if board[y+j][x+i] == val:
                    return False
    return True

