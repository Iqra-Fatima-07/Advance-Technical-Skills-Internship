'''
Problem 67 — Find the Intersection Node of Two Linked Lists

Difficulty: Medium

Topic: Linked List, Two Pointers

Problem Statement

Two singly linked lists may eventually merge and share the same nodes.

Given the two lists, determine the first common node shared by both lists.

If the lists do not intersect, print -1.

Input Format

First line contains N and M.

Second line contains N values for the first list.

Third line contains M values for the second list.

Fourth line contains integer P, representing the index in the first list from which the second list joins.

Output Format

Print the value of the first common node, or -1.

Constraints

1 ≤ N, M ≤ 10^5
-1 ≤ P < N

Sample Input

5 4
4 1 8 4 5
5 6 8 4
2

Sample Output

8

Sample Explanation

The second list joins the first list at node 8. Therefore, 8 is the first common node.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = int(input())

head1 = Node(a[0])
current = head1

nodes = [head1]

for value in a[1:]:
    current.next = Node(value)
    current = current.next
    nodes.append(current)

head2 = Node(b[0])
current = head2

for value in b[1:]:
    current.next = Node(value)
    current = current.next

if p >= 0:
    current = head2

    while current.next is not None:
        current = current.next

    current.next = nodes[p]

ptr1 = head1
ptr2 = head2

while ptr1 is not ptr2:
    ptr1 = ptr1.next if ptr1 else head2
    ptr2 = ptr2.next if ptr2 else head1

if ptr1:
    print(ptr1.value)
else:
    print(-1)