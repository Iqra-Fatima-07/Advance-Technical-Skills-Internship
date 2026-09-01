'''
Problem 34 — Generate All Valid Parentheses

Topic: Backtracking

Problem Statement

Given N pairs of parentheses, generate every possible sequence containing exactly N opening parentheses and N closing parentheses such that the sequence is valid.

A sequence is valid if, while scanning from left to right, the number of closing parentheses never exceeds the number of opening parentheses, and both counts are equal at the end.

Print all valid sequences in lexicographic order.

Input Format

The input contains one integer N.

Output Format

First print the number of valid sequences.

Then print each valid sequence on a separate line in lexicographic order.

Constraints

1 ≤ N ≤ 10

Sample Input

3

Sample Output

5
((()))
(()())
(())()
()(())
()()()

Sample Explanation

There are exactly five valid sequences containing three pairs of parentheses.
'''

n = int(input())

result = []

def generate(open_count, close_count, current):
    if len(current) == 2 * n:
        result.append(''.join(current))
        return

    if open_count < n:
        current.append('(')
        generate(open_count + 1, close_count, current)
        current.pop()

    if close_count < open_count:
        current.append(')')
        generate(open_count, close_count + 1, current)
        current.pop()

generate(0, 0, [])

print(len(result))

for sequence in result:
    print(sequence) 