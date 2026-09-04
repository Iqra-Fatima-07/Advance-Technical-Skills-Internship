'''
Problem 69 — Reorder a Linked List

Difficulty: Medium

Topic: Linked List, Two Pointers

Problem Statement

Given a linked list:

L1 → L2 → L3 → ... → Ln

reorder it as:

L1 → Ln → L2 → Ln-1 → L3 → ...

The node values must not be changed; only the links between nodes may be modified.

Input Format

First line contains integer N.

Second line contains N integers.

Output Format

Print the reordered linked list.

Constraints

1 ≤ N ≤ 10^5
-10^9 ≤ node value ≤ 10^9

Sample Input

6
1 2 3 4 5 6

Sample Output

1 6 2 5 3 4
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


n = int(input())
values = list(map(int, input().split()))

head = Node(values[0])
current = head

for value in values[1:]:
    current.next = Node(value)
    current = current.next

slow = head
fast = head

while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next

second = slow.next
slow.next = None

prev = None

while second:
    next_node = second.next
    second.next = prev
    prev = second
    second = next_node

first = head
second = prev

while second:
    first_next = first.next
    second_next = second.next

    first.next = second
    second.next = first_next

    first = first_next
    second = second_next

result = []
current = head

while current:
    result.append(current.value)
    current = current.next

print(*result)