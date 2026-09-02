'''
Problem 50 — Find the First Non-Repeating Character

Topic: Strings, Hashing

Problem Statement

Given a string, find the first character that occurs exactly once in the entire string.

If no such character exists, print -1.

Input Format

A single line containing string S.

Output Format

Print the first non-repeating character.

Constraints

1 ≤ |S| ≤ 10^5

String contains lowercase English letters.

Sample Input

swiss

Sample Output

w

Sample Explanation

The frequencies are:

s → 3

w → 1

i → 1

w is the first character with frequency 1.
'''

s = input().strip()

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
else:
    print(-1)