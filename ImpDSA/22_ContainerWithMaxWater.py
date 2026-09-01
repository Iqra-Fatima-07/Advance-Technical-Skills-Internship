'''
Problem 22 — Container with Maximum Water

Topic: Two Pointers

Problem Statement

You are given N vertical lines positioned at consecutive integer coordinates. The height of line i is A[i].

Choose two different lines to form a container. The container's capacity is the distance between the two lines multiplied by the smaller of their heights.

Find the maximum possible capacity.

Input Format

The first line contains N.

The second line contains N positive integers representing line heights.

Output Format

Print the maximum possible container capacity.

Constraints

2 ≤ N ≤ 2 × 10^5
0 ≤ A[i] ≤ 10^9

Sample Input

9
1 8 6 2 5 4 8 3 7

Sample Output

49

Sample Explanation

Choosing the lines at indices 1 and 8 gives width 7 and minimum height 7.

Therefore:

7 × 7 = 49
'''

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
max_capacity = 0

while left < right:
    width = right - left
    height = min(arr[left], arr[right])

    capacity = width * height
    max_capacity = max(max_capacity, capacity)

    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1

print(max_capacity)