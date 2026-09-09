'''
Problem 60 — Kth Largest Element

Topic: Heap, Arrays

Problem Statement:

Given an unsorted array and an integer K, find the Kth largest element.

Duplicate values are counted separately.

For example, in [5, 3, 5, 2], the 2nd largest element is 5.

Input Format:

First line contains integer N.

Second line contains N integers.

Third line contains integer K.

Output Format:

Print the Kth largest element.

Constraints:

1 ≤ K ≤ N ≤ 10^5

-10^9 ≤ arr[i] ≤ 10^9

Sample Input:

6
3 2 1 5 6 4
2

Sample Output:

5

Sample Explanation:

The elements in descending order are:

6, 5, 4, 3, 2, 1

Therefore, the 2nd largest element is 5.
'''

import heapq

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

heap = []

for num in arr:
    heapq.heappush(heap, num)

    if len(heap) > k:
        heapq.heappop(heap)

print(heap[0])