def solve_maze(maze):
    n = len(maze)
    solution = [[0] * n for _ in range(n)]

    def is_safe(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

    def backtrack(x, y):
        if x == n - 1 and y == n - 1 and maze[x][y] == 1:
            solution[x][y] = 1
            return True

        if is_safe(x, y):
            if solution[x][y] == 1:
                return False

            solution[x][y] = 1

            if backtrack(x + 1, y):
                return True
            if backtrack(x, y + 1):
                return True

            solution[x][y] = 0
            return False

        return False

    if backtrack(0, 0):
        for row in solution:
            print(" ".join(map(str, row)))
    else:
        print("No solution exists")


maze_template = [
    "1000",
    "1101",
    "0100",
    "1111"
]


maze = [[int(char) for char in row] for row in maze_template]

solve_maze(maze)
