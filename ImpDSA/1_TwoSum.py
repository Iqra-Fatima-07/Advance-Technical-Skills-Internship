'''
1. Two Sum with Indices

ARRAYS & HASHING

Given an integer array and a target value, find two distinct elements whose sum is exactly equal to the target. Return their zero-based indices.

The same array position cannot be used twice. Exactly one valid pair is guaranteed.

INPUT FORMAT:

Line 1: N T
Line 2: N space-separated integers

SAMPLE INPUT

6 9
2 7 11 15 3 4

OUTPUT FORMAT:

Print the two zero-based indices in increasing order.

SAMPLE OUTPUT

0 1

EXPLANATION:

A[0] + A[1] = 2 + 7 = 9.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
-10^9 ≤ A[i], T ≤ 10^9

'''



n, target = map(int, input().split())
arr = list(map(int, input().split()))

seen = {}

for i in range(n):
    need = target - arr[i]

    if need in seen:
        print(seen[need], i)
        break

    seen[arr[i]] = i