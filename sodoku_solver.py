def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    return None,None

def valid(puzzle,guess,row,col):
    row_val = puzzle[row] #row
    if guess in row_val:
        return False
    
    col_val = [puzzle[row][i] for i in range(9)]  #column
    if guess in col_val:
        return False
    
    box_start_r = row//3 * 3
    box_start_c = col//3 * 3

    for i in range(box_start_r,box_start_r + 3):
        for j in range(box_start_c,box_start_c + 3):
            if puzzle[i][j] == guess:
                return False
    return True


def solve_sodoku(puzzle):
    row, col = find_next_empty(puzzle)
    if row == None:
        return True
    for guess in range(1,10):
        if valid(puzzle,guess,row,col):
            puzzle[row][col] = guess
            if solve_sodoku(puzzle):
                return True
    puzzle[row][col] = -1
    return False

example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

print(solve_sodoku(example_board))
print(example_board)

