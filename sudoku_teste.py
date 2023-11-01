from utils_solver_sudoku import is_valid_cross, is_valid_square



def free_slot(board):
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == ".": return (y,x)

def recur(board):
    try:
        y, x = free_slot(board)
    except:
        return True
    for i in range(9):
        pick = str(i+1)
        if is_valid_cross(board, (y,x), pick) and is_valid_square(board, (y,x), pick):
            board[y][x] = pick
            if recur(board): return True
            board[y][x] = "."
        
def sudoku_printer(board):
    style = "\u001b[1m\u001b[47;1m\033[1m\033[96m"
    reset = "\u001b[0m"
    giga_count = 0
    for _ in range(25):
        print(style + "-", end="")
    print(reset)        
    for row in board:
        print(style, end="")
        print("|",end=" ")
        count = 0
        for n in row:
            print(n, end=" ")
            count += 1
            if count%3==0:
                if count == 9: print("|" + reset, end="")
                else:
                    print("|",end=" ")
        giga_count += 1
        print()
        if giga_count == 3:
            giga_count = 0
            for _ in range(25):
                print(style + "-", end="")
            print(reset)
    print(reset)

def parse_board():
    with open('inp.txt') as f:
        board = []
        for line in f:
            if line.strip() == "": 
                yield board
                board.clear()
            else:
                board.append([c if c != "0" else "." for c in line.strip()])
        yield board


def main():
    for board in parse_board():
        recur(board)
        sudoku_printer(board)

if __name__=="__main__":
    main()
    