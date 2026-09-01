'''
Problem 38 — Split Array into K Equal-Sum Parts

Topic: Prefix Sum / Greedy

Problem Statement

Given an integer array, determine whether it can be divided into exactly K contiguous, non-empty parts such that every part has the same sum.

The order of elements must remain unchanged, and every element must belong to exactly one part.

Input Format

The first line contains N and K.

The second line contains N integers.

Output Format

Print YES if such a partition exists; otherwise print NO.

Constraints

1 ≤ K ≤ N ≤ 2 × 10^5

−10^9 ≤ A[i] ≤ 10^9

Sample Input

6 2
1 1 2 2 1 1

Sample Output

YES

Sample Explanation

The array can be divided into:

[1,1,2] and [2,1,1]

Both parts have sum 4.
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

total = sum(arr)

if total % k != 0:
    print("NO")
else:
    target = total // k
    current_sum = 0
    parts = 0
    possible = True

    for num in arr:
        current_sum += num

        if current_sum == target:
            parts += 1
            current_sum = 0

    if parts == k and current_sum == 0:
        print("YES")
    else:
        print("NO")