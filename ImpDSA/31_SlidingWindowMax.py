'''
Problem 31 — Sliding Window Maximum

Topic: Deque / Sliding Window

Problem Statement

Given an integer array and a window size K, determine the maximum element in every contiguous window of exactly K elements.

The windows are considered from left to right, beginning with indices 0 through K-1.

Input Format

First line contains N and K.

Second line contains N integers.

Output Format

Print the maximum value from each window in order.

Constraints

1 ≤ K ≤ N ≤ 2 × 10^5

−10^9 ≤ A[i] ≤ 10^9

Sample Input

8 3
1 3 -1 -3 5 3 6 7

Sample Output

3 3 5 5 6 7

Sample Explanation

The first window is [1,3,-1], whose maximum is 3.

The next window is [3,-1,-3], whose maximum is also 3.

Continuing this process produces the remaining values.
'''

from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()
result = []

for i in range(n):
    while dq and dq[0] <= i - k:
        dq.popleft()

    while dq and arr[dq[-1]] <= arr[i]:
        dq.pop()

    dq.append(i)

    if i >= k - 1:
        result.append(arr[dq[0]])

print(*result)