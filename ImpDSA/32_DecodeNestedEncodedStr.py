'''
Problem 32 — Decode Nested Encoded String

Topic: Stack / String Parsing

Problem Statement

An encoded string follows the format k[encoded_text], where k is a positive integer and encoded_text must be repeated exactly k times.

Encoded sections may be nested. For example, 2[a3[b]] means that a3[b] is repeated twice.

Decode the complete string.

Input Format

The input contains one valid encoded string.

The string contains lowercase English letters, digits, and square brackets.

Digits always represent positive repetition counts.

Output Format

Print the decoded string.

Constraints

1 ≤ encoded length ≤ 2 × 10^5

The decoded output length does not exceed 10^6.

Sample Input

3[a2[c]]

Sample Output

accaccacc

Sample Explanation

2[c] becomes cc.

Therefore a2[c] becomes acc.

Repeating it three times produces accaccacc.
'''

s = input().strip()

count_stack = []
string_stack = []

current = []
number = 0

for ch in s:
    if ch.isdigit():
        number = number * 10 + int(ch)

    elif ch == '[':
        count_stack.append(number)
        string_stack.append(current)

        number = 0
        current = []

    elif ch == ']':
        repeat = count_stack.pop()
        previous = string_stack.pop()

        current = previous + current * repeat

    else:
        current.append(ch)

print(''.join(current))