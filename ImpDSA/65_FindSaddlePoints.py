'''
Problem 65 — Find Saddle Points in a Matrix

Difficulty: Medium

Topic: Matrix, Arrays

Problem Statement

An element is called a saddle point if it is the smallest element in its row and simultaneously the largest element in its column.

Find all saddle points in the given matrix.

Input Format

First line contains N and M.

Next N lines contain M integers.

Output Format

Print each saddle point as:

value row column

Use zero-based row and column indices.

If no saddle point exists, print -1.

Constraints

1 ≤ N, M ≤ 500
-10^6 ≤ A[i][j] ≤ 10^6

Sample Input

3 3
3 1 4
5 6 7
8 2 9

Sample Output

-1
'''

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# Maximum value of every column
column_max = [-10**18] * m

for j in range(m):
    for i in range(n):
        column_max[j] = max(column_max[j], matrix[i][j])

result = []

for i in range(n):
    row_min = min(matrix[i])

    for j in range(m):
        if matrix[i][j] == row_min and matrix[i][j] == column_max[j]:
            result.append((matrix[i][j], i, j))

if result:
    for value, row, col in result:
        print(value, row, col)
else:
    print(-1)