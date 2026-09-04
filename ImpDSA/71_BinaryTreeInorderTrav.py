'''
Problem 71 — Binary Tree Inorder Traversal Without Recursion

Difficulty: Medium

Topic: Binary Tree, Stack

Problem Statement

Given a binary tree, print its inorder traversal without using recursion.

Inorder traversal visits:

Left → Root → Right

The tree is given in level-order representation, where -1 represents a missing child.

Input Format

First line contains integer N.

Second line contains N level-order values.

-1 represents a null node.

Output Format

Print the inorder traversal.

Constraints

1 ≤ N ≤ 10^5

Sample Input

7
1 2 3 4 5 6 7

Sample Output

4 2 5 1 6 3 7
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

    stack = []
    current = root
    result = []

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.value)
        current = current.right

    print(*result)