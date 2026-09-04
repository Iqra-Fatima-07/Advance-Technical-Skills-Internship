'''
Problem 73 — Count Nodes at a Given Level

Difficulty: Medium

Topic: Binary Tree, BFS

Problem Statement

Given a binary tree and an integer K, determine how many nodes exist at level K.

The root is considered to be at level 0.

Input Format

First line contains integer N.

Second line contains the level-order representation.

Third line contains integer K.

Output Format

Print the number of nodes at level K.

Constraints

1 ≤ N ≤ 10^5
0 ≤ K ≤ 10^5

Sample Input

7
1 2 3 4 5 6 7
2

Sample Output

4

Sample Explanation

Level 0 contains 1.

Level 1 contains 2,3.

Level 2 contains 4,5,6,7.

Therefore, there are 4 nodes at level 2.
'''

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


n = int(input())
values = list(map(int, input().split()))
k = int(input())

if values[0] == -1:
    print(0)
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
    level = 0

    while queue and level < k:
        size = len(queue)

        for _ in range(size):
            current = queue.popleft()

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        level += 1

    if level == k:
        print(len(queue))
    else:
        print(0)