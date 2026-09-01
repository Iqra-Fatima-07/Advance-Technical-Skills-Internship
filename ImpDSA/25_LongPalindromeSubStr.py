'''
Problem 25 — Longest Palindromic Substring

Topic: Strings / Dynamic Programming

Problem Statement

Given a string S, find the longest contiguous substring that reads the same from left to right and right to left.

If multiple palindromic substrings have the same maximum length, return the one with the smallest starting index.

Input Format

The input contains one string S.

Output Format

Print the longest palindromic substring.

Constraints

1 ≤ |S| ≤ 5000

S contains lowercase English letters.

Sample Input

babad

Sample Output

bab

Sample Explanation

Both bab and aba have length 3, but bab starts at the smaller index, so it is selected.
'''

s = input().strip()
n = len(s)

dp = [[False] * n for _ in range(n)]

best_start = 0
best_length = 1

for i in range(n):
    dp[i][i] = True

for length in range(2, n + 1):
    for start in range(n - length + 1):
        end = start + length - 1

        if s[start] == s[end]:
            if length == 2 or dp[start + 1][end - 1]:
                dp[start][end] = True

                if length > best_length:
                    best_length = length
                    best_start = start

print(s[best_start:best_start + best_length])