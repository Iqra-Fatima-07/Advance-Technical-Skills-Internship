'''
15. Maximum Circular Subarray Sum

Treat the array as circular, meaning the last element is adjacent to the first. Find the maximum sum of a non-empty contiguous subarray, including a subarray that wraps around.

INPUT FORMAT

Line 1: N
Line 2: N integers

SAMPLE INPUT

5
5 -3 5 -2 4

OUTPUT FORMAT

Print the maximum circular subarray sum.

SAMPLE OUTPUT

11

EXPLANATION

The wrapping subarray [4,5,-3,5] has sum 11.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
-10^9 ≤ A[i] ≤ 10^9
'''

n = int(input())
arr = list(map(int, input().split()))

total = arr[0]

current_max = arr[0]
max_sum = arr[0]

current_min = arr[0]
min_sum = arr[0]

for i in range(1, n):
    num = arr[i]

    current_max = max(num, current_max + num)
    max_sum = max(max_sum, current_max)

    current_min = min(num, current_min + num)
    min_sum = min(min_sum, current_min)

    total += num

if max_sum < 0:
    print(max_sum)
else:
    circular_sum = total - min_sum
    print(max(max_sum, circular_sum))