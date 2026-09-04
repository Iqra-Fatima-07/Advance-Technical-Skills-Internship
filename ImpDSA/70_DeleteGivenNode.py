'''
Problem 70 — Delete a Node Given Only That Node

Difficulty: Medium

Topic: Linked List

Problem Statement

You are given a singly linked list and a reference to a node that must be deleted.

You are not given the head of the list.

The given node is guaranteed not to be the last node.

Delete the given node from the linked list.

Input Format

First line contains integer N.

Second line contains N node values.

Third line contains zero-based index P of the node to delete.

Output Format

Print the linked list after deletion.

Constraints

2 ≤ N ≤ 10^5
0 ≤ P < N-1

Sample Input

5
4 5 1 9 7
2

Sample Output

4 5 9 7
'''

n = int(input())
values = list(map(int, input().split()))
p = int(input())

values[p] = values[p + 1]

for i in range(p + 1, n - 1):
    values[i] = values[i + 1]

print(*values[:-1])