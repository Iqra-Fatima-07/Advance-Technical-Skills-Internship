'''
2. Longest Consecutive Sequence

HASHING:

Given an unsorted array of integers, find the length of the longest sequence of consecutive integer values.

The elements do not need to be adjacent in the original array. Duplicate values do not increase the sequence length.

INPUT FORMAT:

Line 1: N
Line 2: N integers

SAMPLE INPUT:

6
100 4 200 1 3 2

OUTPUT FORMAT:

Print the length of the longest consecutive sequence.

SAMPLE OUTPUT:

4

EXPLANATION:

1, 2, 3, 4 form the longest consecutive sequence.

CONSTRAINTS:

1 ≤ N ≤ 2 × 10^5
-10^9 ≤ A[i] ≤ 10^9
'''

n = int(input())
arr = list(map(int, input().split()))

nums = set(arr)
longest = 0

for num in nums:
    if num - 1 not in nums:
        current = num
        length = 1

        while current + 1 in nums:
            current += 1
            length += 1

        longest = max(longest, length)

print(longest)
