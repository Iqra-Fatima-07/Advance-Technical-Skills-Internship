'''
Problem 72 — Zigzag Level Order Traversal

Difficulty: Medium

Topic: Binary Tree, Queue

Problem Statement

Given a binary tree, print its nodes level by level in alternating directions.

The first level is printed from left to right, the second from right to left, and so on.

Input Format

First line contains integer N.

Second line contains the level-order representation of the tree.

-1 represents a missing node.

Output Format

Print each level on a separate line.

Constraints

1 ≤ N ≤ 10^5

Sample Input

7
1 2 3 4 5 6 7

Sample Output

1
3 2
4 5 6 7
'''

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


n = int(input())
values = list(map(int, input().split()))

if values[0] == -1:
    print()
else:
    root = Node(values[0])
    queue = deque([root])
    index = 1

    while queue and index < n:
        current = queue.popleft()

        if index < n and values[index] != -1:
            current.left = Node(values[index])
            queue.append(current.left)
        index += 1

        if index < n and values[index] != -1:
            current.right = Node(values[index])
            queue.append(current.right)
        index += 1

    queue = deque([root])
    left_to_right = True

    while queue:
        size = len(queue)
        level = []

        for _ in range(size):
            current = queue.popleft()
            level.append(current.value)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        if not left_to_right:
            level.reverse()

        print(*level)
        left_to_right = not left_to_right