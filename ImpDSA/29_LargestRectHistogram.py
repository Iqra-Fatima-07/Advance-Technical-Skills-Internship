'''
Problem 29 — Largest Rectangle in a Histogram

Topic: Monotonic Stack

Problem Statement

A histogram contains N adjacent bars, where bar i has height H[i] and width 1.

Find the largest rectangular area that can be formed using one or more consecutive bars. The rectangle's height cannot exceed the height of any bar it covers.

Input Format

First line contains N.

Second line contains N non-negative integers representing bar heights.

Output Format

Print the maximum rectangular area.

Constraints

1 ≤ N ≤ 2 × 10^5

0 ≤ H[i] ≤ 10^9

Sample Input

6
2 1 5 6 2 3

Sample Output

10

Sample Explanation

Bars with heights 5 and 6 form a rectangle of height 5 and width 2.

Therefore the area is:

5 × 2 = 10.
'''

n = int(input())
heights = list(map(int, input().split()))

stack = []
max_area = 0

for i in range(n + 1):
    current_height = 0 if i == n else heights[i]

    while stack and heights[stack[-1]] > current_height:
        height = heights[stack.pop()]

        if stack:
            width = i - stack[-1] - 1
        else:
            width = i

        max_area = max(max_area, height * width)

    stack.append(i)

print(max_area)