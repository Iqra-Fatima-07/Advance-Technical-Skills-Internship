'''
Problem 57 — Search in a Rotated Sorted Array

Topic: Binary Search, Arrays

Problem Statement

A sorted array has been rotated at an unknown position.

Given the rotated array and a target value, find the index of the target using an efficient search technique.

Assume all elements are distinct.

Input Format

First line contains integer N.

Second line contains N integers.

Third line contains target X.

Output Format

Print the zero-based index of X. If it does not exist, print -1.

Constraints

1 ≤ N ≤ 10^5

All array elements are distinct.

-10^9 ≤ arr[i], X ≤ 10^9

Sample Input

7
6 7 8 1 2 3 4
3

Sample Output

5
'''

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

left = 0
right = n - 1
answer = -1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == x:
        answer = mid
        break

    # Left half is sorted
    if arr[left] <= arr[mid]:
        if arr[left] <= x < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # Right half is sorted
    else:
        if arr[mid] < x <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1

print(answer)