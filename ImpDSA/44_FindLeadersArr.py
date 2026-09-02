'''
Problem 44 — Find Leaders in an Array

Topic: Arrays

Problem Statement

An element is called a leader if it is greater than or equal to every element appearing to its right.

The last element is always considered a leader.

Find all leaders in the array and print them in their original left-to-right order.

Input Format

First line contains integer N.

Second line contains N integers.

Output Format

Print all leader elements.

Constraints

1 ≤ N ≤ 10^5
-10^6 ≤ arr[i] ≤ 10^6

Sample Input

7
16 17 4 3 5 2 1

Sample Output

17 5 2 1

Sample Explanation

17 is greater than all elements to its right. Similarly, 5, 2, and 1 satisfy the condition.
'''

n = int(input())
arr = list(map(int, input().split()))

leaders = []
max_right = arr[-1]

leaders.append(max_right)

for i in range(n - 2, -1, -1):
    if arr[i] >= max_right:
        leaders.append(arr[i])
        max_right = arr[i]

leaders.reverse()

print(*leaders)