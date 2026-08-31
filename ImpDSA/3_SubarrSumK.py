'''
3. Subarray Sum Equals K

PREFIX SUM & HASHING

Given an integer array and an integer K, count the number of contiguous, non-empty subarrays whose sum is exactly K.

The array may contain positive, negative, and zero values.

INPUT FORMAT

Line 1: N K
Line 2: N integers

SAMPLE INPUT

5 3
1 2 1 1 1

OUTPUT FORMAT

Print the total number of qualifying subarrays.

SAMPLE OUTPUT

3

EXPLANATION

[1, 2], [2, 1], and [1, 1, 1] each have sum 3.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
-10^9 ≤ A[i], K ≤ 10^9


'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = 0
count = 0
freq = {0: 1}

for num in arr:
    prefix_sum += num

    if prefix_sum - k in freq:
        count += freq[prefix_sum - k]

    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

print(count)