'''
12. Longest Subarray with At Most K Distinct Values

Find the maximum length of a contiguous subarray containing at most K distinct values.

INPUT FORMAT

Line 1: N K
Line 2: N integers

SAMPLE INPUT

7 2
1 2 1 2 3 2 2

OUTPUT FORMAT

Print the maximum valid length. If K=0, print 0.

SAMPLE OUTPUT

4

EXPLANATION

[1,2,1,2] contains exactly 2 distinct values and has length 4.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
0 ≤ K ≤ N
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k == 0:
    print(0)
else:
    freq = {}
    left = 0
    answer = 0

    for right in range(n):
        freq[arr[right]] = freq.get(arr[right], 0) + 1

        while len(freq) > k:
            freq[arr[left]] -= 1

            if freq[arr[left]] == 0:
                del freq[arr[left]]

            left += 1

        answer = max(answer, right - left + 1)

    print(answer)