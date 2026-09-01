'''
Problem 36 — Kth Smallest Pair Distance

Topic: Binary Search / Two Pointers

Problem Statement

Given an integer array, consider every unordered pair of indices (i,j) where i < j. The distance of a pair is:

|A[i] - A[j]|

Find the Kth smallest pair distance when all pair distances are sorted in non-decreasing order.

Duplicate distances are counted separately.

Input Format

The first line contains N and K.

The second line contains N integers.

Output Format

Print the Kth smallest pair distance.

Constraints

2 ≤ N ≤ 2 × 10^5

1 ≤ K ≤ N(N−1)/2

0 ≤ A[i] ≤ 10^9

Sample Input

4 3
1 3 1 4

Sample Output

2

Sample Explanation

The pair distances are:

0, 1, 2, 2, 3, 3

The third smallest distance is 2.
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = arr[-1] - arr[0]

while left < right:
    mid = (left + right) // 2

    count = 0
    j = 0

    for i in range(n):
        while j < n and arr[j] - arr[i] <= mid:
            j += 1

        count += j - i - 1

    if count >= k:
        right = mid
    else:
        left = mid + 1

print(left)