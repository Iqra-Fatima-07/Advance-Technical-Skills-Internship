'''
Problem 68 — Add Two Numbers Represented by Linked Lists

Difficulty: Medium

Topic: Linked List, Arithmetic

Problem Statement

Two non-negative integers are represented by singly linked lists, where each node contains one digit.

The digits are stored from most significant to least significant.

Add the two numbers and return the result as a linked list in the same format.

Input Format

First line contains N.

Second line contains N digits of the first number.

Third line contains M.

Fourth line contains M digits of the second number.

Output Format

Print the digits of the resulting number.

Constraints

1 ≤ N, M ≤ 10^5
Each digit is between 0 and 9.

Sample Input

3
7 2 4
3
5 6 4

Sample Output

1 2 8 8

Sample Explanation

724 + 564 = 1288
'''

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

i = n - 1
j = m - 1
carry = 0
result = []

while i >= 0 or j >= 0 or carry:
    total = carry

    if i >= 0:
        total += a[i]
        i -= 1

    if j >= 0:
        total += b[j]
        j -= 1

    result.append(total % 10)
    carry = total // 10

result.reverse()

print(*result)