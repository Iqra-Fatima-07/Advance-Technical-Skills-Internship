'''
Problem 35 — N-Queens Count

Topic: Backtracking

Problem Statement

Place N queens on an N × N chessboard such that no two queens attack each other.

Two queens attack each other if they share:

The same row
The same column
The same diagonal

Determine the total number of distinct valid arrangements.

Two arrangements are considered different if at least one queen occupies a different cell.

Input Format

The input contains one integer N.

Output Format

Print the total number of valid arrangements.

Constraints

1 ≤ N ≤ 14

Sample Input

4

Sample Output

2

Sample Explanation

For a 4 × 4 board, exactly two distinct arrangements satisfy all constraints.
'''

n = int(input())

count = 0

columns = set()
diagonal1 = set()
diagonal2 = set()

def solve(row):
    global count

    if row == n:
        count += 1
        return

    for col in range(n):
        if col in columns:
            continue

        if row - col in diagonal1:
            continue

        if row + col in diagonal2:
            continue

        columns.add(col)
        diagonal1.add(row - col)
        diagonal2.add(row + col)

        solve(row + 1)

        columns.remove(col)
        diagonal1.remove(row - col)
        diagonal2.remove(row + col)

solve(0)

print(count)