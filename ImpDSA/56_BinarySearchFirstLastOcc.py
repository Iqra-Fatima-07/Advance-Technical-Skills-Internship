'''
Problem 56 — Binary Search for First and Last Occurrence

Topic: Binary Search

Problem Statement

Given a sorted array that may contain duplicate values and a target value X, find the first and last occurrence of X.

If X does not exist, print -1 -1.

Input Format

First line contains integer N.

Second line contains N sorted integers.

Third line contains integer X.

Output Format

Print the zero-based indices of the first and last occurrence.

Constraints

1 ≤ N ≤ 10^5

Array is sorted in non-decreasing order.

-10^9 ≤ arr[i], X ≤ 10^9

Sample Input

8
1 2 2 2 3 4 4 5
2

Sample Output

1 3
'''

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

def first_occurrence():
    left = 0
    right = n - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            answer = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return answer

def last_occurrence():
    left = 0
    right = n - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            answer = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return answer

first = first_occurrence()
last = last_occurrence()

print(first, last)