'''
Problem 61 — Spiral Traversal of a Matrix

Difficulty: Medium

Topic: Matrix, Arrays

Problem Statement

Given an N × M matrix, print all its elements in spiral order.

The traversal should begin from the top-left corner and move:
Left to right
Top to bottom
Right to left
Bottom to top

Continue until every element has been visited.

Input Format

First line contains N and M.

Next N lines contain M integers each.

Output Format

Print all matrix elements in spiral order.

Constraints

1 ≤ N, M ≤ 500
-10^6 ≤ A[i][j] ≤ 10^6

Sample Input

3 4
1 2 3 4
5 6 7 8
9 10 11 12

Sample Output

1 2 3 4 8 12 11 10 9 5 6 7
'''

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

top = 0
bottom = n - 1
left = 0
right = m - 1

result = []

while top <= bottom and left <= right:

    for j in range(left, right + 1):
        result.append(matrix[top][j])
    top += 1

    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        for j in range(right, left - 1, -1):
            result.append(matrix[bottom][j])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(*result)