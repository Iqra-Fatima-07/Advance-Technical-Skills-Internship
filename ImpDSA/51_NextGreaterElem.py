'''
Problem 51 — Next Greater Element

Topic: Stack, Arrays

Problem Statement

For every element in an array, find the first element to its right that is strictly greater than it.

If no greater element exists, print -1.

Input Format

First line contains integer N.

Second line contains N integers.

Output Format

Print the next greater element for every array element.

Constraints

1 ≤ N ≤ 10^5
-10^9 ≤ arr[i] ≤ 10^9

Sample Input

6
4 5 2 10 8 7

Sample Output

5 10 10 -1 -1 -1
'''

n = int(input())
arr = list(map(int, input().split()))

result = [-1] * n
stack = []

for i in range(n - 1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1]

    stack.append(arr[i])

print(*result)