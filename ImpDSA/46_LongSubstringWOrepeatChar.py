'''
Problem 46 — Longest Substring Without Repeating Characters

Topic: Strings, Sliding Window

Problem Statement

Given a string, find the length of the longest substring that contains no repeated characters.

The substring must contain consecutive characters.

Input Format

A single line containing a string S.

Output Format

Print the length of the longest substring without repeated characters.

Constraints

1 ≤ |S| ≤ 10^5

The string contains printable ASCII characters.

Sample Input

abcabcbb

Sample Output

3

Sample Explanation

The longest substring without repeating characters is "abc", whose length is 3.
'''

s = input().rstrip()

last_seen = {}
left = 0
answer = 0

for right in range(len(s)):
    ch = s[right]

    if ch in last_seen and last_seen[ch] >= left:
        left = last_seen[ch] + 1

    last_seen[ch] = right

    answer = max(answer, right - left + 1)

print(answer)