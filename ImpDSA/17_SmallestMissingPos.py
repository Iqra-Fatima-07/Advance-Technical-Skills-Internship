'''
17. Smallest Missing Positive

Find the smallest positive integer that does not appear in the array. The array may contain negative values, zero, duplicates, and values larger than N.

INPUT FORMAT

Line 1: N
Line 2: N integers

SAMPLE INPUT

5
3 4 -1 1 2

OUTPUT FORMAT

Print the smallest missing positive integer.

SAMPLE OUTPUT

5

EXPLANATION

1, 2, 3, 4 are present, so 5 is the smallest missing positive.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
-10^9 ≤ A[i] ≤ 10^9
'''

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
        correct_index = arr[i] - 1
        arr[i], arr[correct_index] = arr[correct_index], arr[i]

for i in range(n):
    if arr[i] != i + 1:
        print(i + 1)
        break
else:
    print(n + 1)