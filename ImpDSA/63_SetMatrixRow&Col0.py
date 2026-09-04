'''
Problem 63 — Set Matrix Rows and Columns to Zero

Difficulty: Medium

Topic: Matrix, Arrays

Problem Statement

Given an N × M matrix, if any element is 0, set its entire row and entire column to 0.

The transformation must be performed in-place, without creating another matrix of the same size.

Input Format

First line contains N and M.

Next N lines contain M integers.

Output Format

Print the transformed matrix.

Constraints

1 ≤ N, M ≤ 500
-10^6 ≤ A[i][j] ≤ 10^6

Sample Input

3 4
1 2 3 4
5 0 7 8
9 10 11 12

Sample Output

1 0 3 4
0 0 0 0
9 0 11 12
'''

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# Use first row and first column as markers
first_row_zero = any(matrix[0][j] == 0 for j in range(m))
first_col_zero = any(matrix[i][0] == 0 for i in range(n))

for i in range(1, n):
    for j in range(1, m):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j] = 0

for i in range(1, n):
    for j in range(1, m):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0

if first_row_zero:
    for j in range(m):
        matrix[0][j] = 0

if first_col_zero:
    for i in range(n):
        matrix[i][0] = 0

for row in matrix:
    print(*row)