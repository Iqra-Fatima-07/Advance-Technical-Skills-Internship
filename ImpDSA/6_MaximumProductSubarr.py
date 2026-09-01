'''
6. Maximum Product Subarray

Find the maximum product obtainable from any non-empty contiguous subarray. The array may contain positive values, negative values, and zero.

INPUT FORMAT

Line 1: N
Line 2: N integers

SAMPLE INPUT

5
2 3 -2 4 -1

OUTPUT FORMAT

Print the maximum product.

SAMPLE OUTPUT

48

EXPLANATION

The entire array has product 48.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
-10 ≤ A[i] ≤ 10
'''

n = int(input())
arr = list(map(int, input().split()))

max_product = arr[0]
min_product = arr[0]
answer = arr[0]

for i in range(1, n):
    num = arr[i]

    if num < 0:
        max_product, min_product = min_product, max_product

    max_product = max(num, max_product * num)
    min_product = min(num, min_product * num)

    answer = max(answer, max_product)

print(answer)