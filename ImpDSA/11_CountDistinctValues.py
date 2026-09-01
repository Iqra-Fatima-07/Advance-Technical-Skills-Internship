'''
11. Count Distinct Values in Every Window

Given an array and a window size K, count the number of distinct values in every contiguous window of exactly K elements.

INPUT FORMAT

Line 1: N K
Line 2: N integers

SAMPLE INPUT

7 3
1 2 1 3 4 2 3

OUTPUT FORMAT

Print N-K+1 distinct counts.

SAMPLE OUTPUT

2 3 3 3 3

EXPLANATION

The first window [1,2,1] contains 2 distinct values.

CONSTRAINTS

1 ≤ K ≤ N ≤ 2 × 10^5
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = {}
result = []

for i in range(k):
    freq[arr[i]] = freq.get(arr[i], 0) + 1

result.append(len(freq))

for i in range(k, n):
    outgoing = arr[i - k]
    freq[outgoing] -= 1

    if freq[outgoing] == 0:
        del freq[outgoing]

    incoming = arr[i]
    freq[incoming] = freq.get(incoming, 0) + 1

    result.append(len(freq))

print(*result)