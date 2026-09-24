'''

4. Longest Zero-Sum Subarray

PREFIX SUM

Find the maximum length of a contiguous, non-empty subarray whose elements sum to zero.

INPUT FORMAT:

Line 1: N
Line 2: N integers

OUTPUT FORMAT:

Print the maximum length.
Print 0 if no valid subarray exists.

SAMPLE INPUT:

6
15 -2 2 -8 1 7

SAMPLE OUTPUT:

5

EXPLANATION:

The subarray [-2, 2, -8, 1, 7] has sum 0 and length 5.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
-10^9 ≤ A[i] ≤ 10^9

'''

n = int(input())
arr = list(map(int, input().split()))

prefix_sum = 0
max_length = 0
first = {0: -1}

for i in range(n):
    prefix_sum += arr[i]

    if prefix_sum in first:
        max_length = max(max_length, i - first[prefix_sum])
    else:
        first[prefix_sum] = i
print(max_length)