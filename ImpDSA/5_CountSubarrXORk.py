'''
5. Count Subarrays with XOR K

Given an array of non-negative integers and a target K, count the number of contiguous, non-empty subarrays whose bitwise XOR is exactly K.

INPUT FORMAT

Line 1: N K
Line 2: N integers

SAMPLE INPUT

5 6
4 2 2 6 4

OUTPUT FORMAT

Print the number of qualifying subarrays.

SAMPLE OUTPUT

2

EXPLANATION

[4, 2] and [2, 6] have XOR equal to 6.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
0 ≤ A[i], K < 2^20
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

xor = 0
count = 0
freq = {0: 1}

for num in arr:
    xor ^= num

    need = xor ^ k

    if need in freq:
        count += freq[need]

    freq[xor] = freq.get(xor, 0) + 1
print(count)