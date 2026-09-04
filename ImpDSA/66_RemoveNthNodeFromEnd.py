'''
Problem 66 — Remove the Nth Node from the End of a Linked List

Difficulty: Medium

Topic: Linked List, Two Pointers

Problem Statement

Given a singly linked list and an integer N, remove the Nth node from the end of the list.

Return the resulting linked list.

Input Format

First line contains integer L.

Second line contains L integers.

Third line contains integer N.

Output Format

Print the linked list after removing the required node.

Constraints

1 ≤ L ≤ 10^5
1 ≤ N ≤ L
-10^9 ≤ node value ≤ 10^9

Sample Input

5
1 2 3 4 5
2

Sample Output

1 2 3 5

Sample Explanation

The 2nd node from the end is 4, so it is removed.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


length = int(input())
values = list(map(int, input().split()))
n = int(input())

# Dummy node makes removing the head easier
dummy = Node(0)

current = dummy

for value in values:
    current.next = Node(value)
    current = current.next

# Move fast N nodes ahead
fast = dummy
slow = dummy

for _ in range(n):
    fast = fast.next

# Move both pointers until fast reaches the last node
while fast.next is not None:
    fast = fast.next
    slow = slow.next

# Remove the Nth node from the end
slow.next = slow.next.next

# Print the resulting list
result = []

current = dummy.next

while current is not None:
    result.append(current.value)
    current = current.next

print(*result)