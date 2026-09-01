'''
16. Count Pairs with Difference K

Count unordered pairs of distinct indices whose values differ by exactly K. Each pair of indices must be counted once.

INPUT FORMAT

Line 1: N K
Line 2: N integers

SAMPLE INPUT

5 2
1 3 5 3 1

OUTPUT FORMAT

Print the total number of valid index pairs.

SAMPLE OUTPUT

4

EXPLANATION

Four distinct index pairs have difference 2.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
0 ≤ K ≤ 10^9
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = {}
count = 0

if k == 0:
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for value in freq:
        count += freq[value] * (freq[value] - 1) // 2
else:
    for num in arr:
        if num - k in freq:
            count += freq[num - k]

        if num + k in freq:
            count += freq[num + k]

        freq[num] = freq.get(num, 0) + 1

print(count)