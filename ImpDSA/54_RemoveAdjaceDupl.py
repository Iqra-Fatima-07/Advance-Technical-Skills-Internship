'''
Problem 54 — Remove Adjacent Duplicates

Topic: Stack, Strings

Problem Statement

Given a string, repeatedly remove pairs of adjacent equal characters.

Continue the process until no adjacent duplicate pair remains.

Return the resulting string. If all characters are removed, print EMPTY.

Input Format

A single line containing string S.

Output Format

Print the resulting string or EMPTY.

Constraints

1 ≤ |S| ≤ 10^5

String contains lowercase English letters.

Sample Input

abbaca

Sample Output

ca

Sample Explanation

bb is removed first:

abbaca → aaca

Then aa is removed:

aaca → ca
'''

s = input().strip()

stack = []

for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)

if stack:
    print(''.join(stack))
else:
    print("EMPTY")