'''
13. Top K Frequent Elements

Given an integer array, find the K values with the highest frequencies. If two values have the same frequency, the smaller value must come first.

INPUT FORMAT

Line 1: N K
Line 2: N integers

SAMPLE INPUT

7 2
1 1 1 2 2 3 4

OUTPUT FORMAT

Print exactly K values in decreasing frequency order. Resolve ties by increasing value.

SAMPLE OUTPUT

1 2

EXPLANATION

1 occurs 3 times and 2 occurs 2 times.

CONSTRAINTS

1 ≤ K ≤ number of distinct values ≤ N ≤ 2 × 10^5
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

values = list(freq.keys())

values.sort(key=lambda x: (-freq[x], x))

print(*values[:k])