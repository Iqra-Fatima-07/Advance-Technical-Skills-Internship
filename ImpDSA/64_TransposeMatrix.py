'''
Problem 64 — Transpose a Matrix

Difficulty: Medium

Topic: Matrix, Arrays

Problem Statement

Given an N × M matrix, construct its transpose.

In the transpose, the element at position (i,j) becomes the element at (j,i).

Input Format

First line contains N and M.

Next N lines contain M integers.

Output Format

Print the transposed matrix with M rows and N columns.

Constraints

1 ≤ N, M ≤ 500
-10^6 ≤ A[i][j] ≤ 10^6

Sample Input

2 3
1 2 3
4 5 6

Sample Output

1 4
2 5
3 6
'''

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for j in range(m):
    row = []

    for i in range(n):
        row.append(matrix[i][j])

    print(*row)