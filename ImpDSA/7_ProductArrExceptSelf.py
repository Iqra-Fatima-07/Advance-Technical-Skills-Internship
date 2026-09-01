'''
7. Product of Array Except Self

For every position i, calculate the product of all array elements except A[i]. Division is not allowed.

INPUT FORMAT

Line 1: N
Line 2: N integers

SAMPLE INPUT

4
1 2 3 4

OUTPUT FORMAT

Print N products in the original order.

SAMPLE OUTPUT

24 12 8 6

EXPLANATION

For index 0, product of all other elements is 2 × 3 × 4 = 24.

CONSTRAINTS

2 ≤ N ≤ 2 × 10^5
-20 ≤ A[i] ≤ 20
'''

n = int(input())
arr = list(map(int, input().split()))

answer = [1] * n

prefix = 1

for i in range(n):
    answer[i] = prefix
    prefix *= arr[i]

suffix = 1

for i in range(n - 1, -1, -1):
    answer[i] *= suffix
    suffix *= arr[i]

print(*answer)