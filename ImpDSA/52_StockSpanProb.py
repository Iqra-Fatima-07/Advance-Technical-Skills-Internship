'''
Problem 52 — Stock Span Problem

Topic: Stack, Arrays

Problem Statement

Given daily stock prices, calculate the stock span for each day.

The span of a day is the number of consecutive days ending on that day for which the stock price was less than or equal to the current day's price.

Input Format

First line contains integer N.

Second line contains N stock prices.

Output Format

Print the span for every day.

Constraints

1 ≤ N ≤ 10^5
1 ≤ price[i] ≤ 10^6

Sample Input

7
100 80 60 70 60 75 85

Sample Output

1 1 1 2 1 4 6
'''

n = int(input())
prices = list(map(int, input().split()))

span = [0] * n
stack = []

for i in range(n):
    while stack and prices[stack[-1]] <= prices[i]:
        stack.pop()

    if stack:
        span[i] = i - stack[-1]
    else:
        span[i] = i + 1

    stack.append(i)

print(*span)