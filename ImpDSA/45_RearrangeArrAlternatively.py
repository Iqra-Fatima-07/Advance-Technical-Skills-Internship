'''
Problem 45 — Rearrange Array Alternately

Topic: Arrays, Two Pointers

Problem Statement

Given a sorted array of positive integers, rearrange it so that the elements appear alternately as:

maximum, minimum, second maximum, second minimum, ...

For example, [1,2,3,4,5] becomes [5,1,4,2,3].

Input Format

First line contains integer N.

Second line contains N sorted integers.

Output Format

Print the rearranged array.

Constraints

1 ≤ N ≤ 10^5
1 ≤ arr[i] ≤ 10^9

Sample Input

6
1 2 3 4 5 6

Sample Output

6 1 5 2 4 3

Sample Explanation

Take the largest element 6, then smallest 1, then second largest 5, then second smallest 2, and so on.
'''

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
result = []

while left <= right:
    result.append(arr[right])
    right -= 1

    if left <= right:
        result.append(arr[left])
        left += 1

print(*result)