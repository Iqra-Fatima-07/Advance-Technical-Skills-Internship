'''
Problem 58 — Find Peak Element

Topic: Binary Search, Arrays

Problem Statement

An element is a peak if it is greater than its immediate neighbors.

For the first and last elements, consider the missing neighbor as negative infinity.

Find any valid peak element and print its index.

Input Format

First line contains integer N.

Second line contains N integers.

Output Format

Print the zero-based index of any peak element.

Constraints

1 ≤ N ≤ 10^5

Adjacent elements are not equal.

-10^9 ≤ arr[i] ≤ 10^9

Sample Input

6
1 3 5 4 2 1

Sample Output

2
'''

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    mid = (left + right) // 2

    if arr[mid] < arr[mid + 1]:
        left = mid + 1
    else:
        right = mid

print(left)