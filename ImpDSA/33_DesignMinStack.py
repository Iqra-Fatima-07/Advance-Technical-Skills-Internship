'''
Problem 33 — Design a Min Stack

Topic: Stack Design

Problem Statement

Design a stack that supports the following operations:

PUSH x — insert integer x.

POP — remove the top element.

TOP — report the top element.

MIN — report the minimum element currently stored.

All operations must behave correctly even when duplicate values are present.

Input Format

The first line contains Q.

Each of the next Q lines contains one operation.

POP, TOP, and MIN are issued only when the stack is non-empty.

Output Format

For every TOP or MIN operation, print the corresponding value on a separate line.

Constraints

1 ≤ Q ≤ 2 × 10^5

−10^9 ≤ x ≤ 10^9

Sample Input

7
PUSH 5
PUSH 2
MIN
PUSH 1
MIN
POP
MIN

Sample Output

2
1
2

Sample Explanation

After pushing 5 and 2, the minimum is 2. After pushing 1, the minimum becomes 1. Removing 1 restores 2 as the minimum.
'''

q = int(input())

stack = []
min_stack = []

for _ in range(q):
    operation = input().split()

    if operation[0] == "PUSH":
        value = int(operation[1])
        stack.append(value)

        if not min_stack:
            min_stack.append(value)
        else:
            min_stack.append(min(value, min_stack[-1]))

    elif operation[0] == "POP":
        stack.pop()
        min_stack.pop()

    elif operation[0] == "TOP":
        print(stack[-1])

    elif operation[0] == "MIN":
        print(min_stack[-1])