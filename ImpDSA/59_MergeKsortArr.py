'''
Problem 59 — Merge K Sorted Arrays

Topic: Heap, Arrays

Problem Statement:

You are given K sorted arrays. Merge all of them into a single sorted array.

The resulting array must contain every element from every input array.

Input Format:

First line contains integer K.

For each array:

First line contains its size N.

Second line contains N sorted integers.

Output Format:

Print all elements in sorted order.

Constraints:

1 ≤ K ≤ 100

Total number of elements ≤ 10^5

Each individual array is sorted.

Sample Input:

3
3
1 4 7
4
2 5 8 10
3
3 6 9

Sample Output:

1 2 3 4 5 6 7 8 9 10
'''

import heapq

k = int(input())

arrays = []

for _ in range(k):
    n = int(input())
    arr = list(map(int, input().split()))
    arrays.append(arr)

heap = []

for i in range(k):
    if arrays[i]:
        heapq.heappush(heap, (arrays[i][0], i, 0))

result = []

while heap:
    value, array_index, element_index = heapq.heappop(heap)
    result.append(value)

    next_index = element_index + 1

    if next_index < len(arrays[array_index]):
        next_value = arrays[array_index][next_index]
        heapq.heappush(heap, (next_value, array_index, next_index))

print(*result)