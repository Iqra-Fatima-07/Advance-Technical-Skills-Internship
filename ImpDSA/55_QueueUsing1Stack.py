'''
Problem 55 — Implement Queue Using One Stack

Topic: Stack, Data Structures, Recursion

Problem Statement

Implement a queue using only one stack and recursion.

The queue must support:

ENQUEUE x
DEQUEUE
FRONT

If DEQUEUE or FRONT is requested when the queue is empty, print EMPTY.

Input Format

First line contains integer Q.

Next Q lines contain operations.

Output Format

For every DEQUEUE or FRONT operation, print the appropriate result.

Constraints

1 ≤ Q ≤ 10^4

Queue values are integers.

Sample Input

6
ENQUEUE 10
ENQUEUE 20
FRONT
DEQUEUE
FRONT
DEQUEUE

Sample Output

10
10
20
20
'''

q = int(input())

stack = []

def get_front():
    value = stack.pop()

    if not stack:
        return value

    front = get_front()
    stack.append(value)

    return front

def remove_front():
    value = stack.pop()

    if not stack:
        return value

    front = remove_front()
    stack.append(value)

    return front

for _ in range(q):
    operation = input().split()

    if operation[0] == "ENQUEUE":
        stack.append(int(operation[1]))

    elif operation[0] == "FRONT":
        if not stack:
            print("EMPTY")
        else:
            front = get_front()
            stack.append(front)
            print(front)

    elif operation[0] == "DEQUEUE":
        if not stack:
            print("EMPTY")
        else:
            print(remove_front())