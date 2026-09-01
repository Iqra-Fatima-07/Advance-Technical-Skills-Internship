'''
14. Longest Arithmetic Subarray

Find the length of the longest contiguous subarray where the difference between every pair of consecutive elements is the same.

INPUT FORMAT

Line 1: N
Line 2: N integers

SAMPLE INPUT

7
10 7 4 1 3 5 7

OUTPUT FORMAT

Print the maximum length.

SAMPLE OUTPUT

4

EXPLANATION

[10,7,4,1] has common difference -3.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
'''

n = int(input())
arr = list(map(int, input().split()))

if n <= 2:
    print(n)
else:
    current_length = 2
    answer = 2

    difference = arr[1] - arr[0]

    for i in range(2, n):
        current_difference = arr[i] - arr[i - 1]

        if current_difference == difference:
            current_length += 1
        else:
            difference = current_difference
            current_length = 2

        answer = max(answer, current_length)

    print(answer)