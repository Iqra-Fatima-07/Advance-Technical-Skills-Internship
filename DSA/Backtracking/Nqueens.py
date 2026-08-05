def solve_n_queens(n):
    board = [["."] * n for _ in range(n)]
    cols = set()
    pos_diag = set()
    neg_diag = set()

    def backtrack(r):
        if r == n:
            for row in board:
                print(" ".join(row))
            print()
            return True

        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"

            if backtrack(r + 1):
                return True

            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

        return False

    if not backtrack(0):
        print("No solution exists")

solve_n_queens(4)
