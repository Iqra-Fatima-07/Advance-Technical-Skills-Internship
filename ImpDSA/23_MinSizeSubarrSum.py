'''
Problem 23 — Minimum Size Subarray with Target Sum

Topic: Sliding Window

Problem Statement

Given an array of positive integers and a positive target T, find the minimum length of a contiguous subarray whose sum is greater than or equal to T.

If no such subarray exists, print 0.

Input Format

The first line contains N and T.

The second line contains N positive integers.

Output Format

Print the minimum length of a qualifying subarray.

Constraints

1 ≤ N ≤ 2 × 10^5
1 ≤ T ≤ 10^15
1 ≤ A[i] ≤ 10^9

Sample Input

6 7
2 3 1 2 4 3

Sample Output

2

Sample Explanation

The subarray [4,3] has sum 7 and length 2. No single element reaches the target, so the minimum length is 2.
'''

n, target = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
current_sum = 0
min_length = n + 1

for right in range(n):
    current_sum += arr[right]

    while current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= arr[left]
        left += 1

if min_length == n + 1:
    print(0)
else:
    print(min_length)