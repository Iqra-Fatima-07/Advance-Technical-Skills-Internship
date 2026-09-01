'''
Problem 28 — Minimum Additions to Make Parentheses Valid

Topic: Stack / Greedy

Problem Statement

You are given a string containing only ( and ) characters.

You may insert parentheses at any position. Determine the minimum number of parentheses that must be inserted so that the entire string becomes a valid balanced-parentheses sequence.

A valid sequence must never have more closing parentheses than opening parentheses in any prefix, and the total number of opening and closing parentheses must be equal.

Input Format

The input contains a string S.

Output Format

Print the minimum number of insertions required.

Constraints

1 ≤ |S| ≤ 2 × 10^5

Sample Input

()))((

Sample Output

4

Sample Explanation

The sequence contains unmatched closing and opening parentheses. Four insertions are sufficient to balance the complete sequence.
'''

s = input().strip()

balance = 0
insertions = 0

for ch in s:
    if ch == '(':
        balance += 1
    else:
        if balance > 0:
            balance -= 1
        else:
            insertions += 1

insertions += balance

print(insertions)