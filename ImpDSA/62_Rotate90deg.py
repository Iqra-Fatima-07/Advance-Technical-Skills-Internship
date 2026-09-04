'''
Problem 62 — Rotate a Matrix by 90 Degrees

Difficulty: Medium

Topic: Matrix, Arrays

Problem Statement

Given a square matrix of size N × N, rotate the matrix 90 degrees clockwise.

The rotation must be performed without creating another N × N matrix.

Input Format

First line contains integer N.

Next N lines contain N integers each.

Output Format

Print the rotated matrix.

Constraints

1 ≤ N ≤ 500
-10^6 ≤ A[i][j] ≤ 10^6

Sample Input

3
1 2 3
4 5 6
7 8 9

Sample Output

7 4 1
8 5 2
9 6 3
'''

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# Transpose the matrix
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Reverse every row
for i in range(n):
    matrix[i].reverse()

for row in matrix:
    print(*row)