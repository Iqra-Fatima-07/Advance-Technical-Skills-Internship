def solve_sudoku(board):
    def is_valid(r, c, val):
        for i in range(9):
            if board[r][i] == val or board[i][c] == val:
                return False
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == val:
                return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for val in range(1, 10):
                        if is_valid(r, c, val):
                            board[r][c] = val
                            if backtrack():
                                return True
                            board[r][c] = 0
                    return False
        return True

    if backtrack():
        for row in board:
            print(" ".join(map(str, row)))
    else:
        print("No solution exists")

# Create a clean 9x9 board with zeros
board = [[0 for _ in range(9)] for _ in range(9)]

# Manually insert a few puzzle numbers to avoid list syntax errors
board[0][0] = 5
board[0][1] = 3
board[0][4] = 7
board[1][0] = 6
board[1][3] = 1
board[1][4] = 9
board[1][5] = 5
board[2][1] = 9
board[2][2] = 8
board[2][7] = 6

solve_sudoku(board)
