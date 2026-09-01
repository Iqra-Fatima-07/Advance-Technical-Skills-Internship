'''
10. Maximum Subarray with One Deletion

Find the maximum sum of a non-empty contiguous subarray when at most one element may be deleted. The deleted element contributes nothing to the sum.

INPUT FORMAT

Line 1: N
Line 2: N integers

SAMPLE INPUT

4
1 -2 0 3

OUTPUT FORMAT

Print the maximum achievable sum.

SAMPLE OUTPUT

4

EXPLANATION

Deleting -2 leaves [1, 0, 3], whose sum is 4.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
-10^9 ≤ A[i] ≤ 10^9
'''

n = int(input())
arr = list(map(int, input().split()))

no_delete = arr[0]
one_delete = float('-inf')
answer = arr[0]

for i in range(1, n):
    num = arr[i]

    new_one_delete = max(one_delete + num, no_delete)
    new_no_delete = max(num, no_delete + num)

    no_delete = new_no_delete
    one_delete = new_one_delete

    answer = max(answer, no_delete, one_delete)

print(answer)