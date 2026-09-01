'''
Problem 27 — Implement KMP Pattern Matching

Topic: String Algorithms / KMP

Problem Statement

Given a text string S and a pattern string P, find every position at which P occurs as a contiguous substring of S.

Occurrences may overlap. For example, if the pattern is aba, it may occur starting at consecutive overlapping positions.

Return all starting positions in increasing order.

Input Format

First line contains S.

Second line contains P.

Both strings contain lowercase English letters.

Output Format

First print the number of occurrences.

On the second line, print all zero-based starting indices.

If there is no occurrence, print 0 followed by -1.

Constraints

1 ≤ |P| ≤ |S| ≤ 10^6

Sample Input

ababa
aba

Sample Output

2
0 2

Sample Explanation

The pattern aba starts at indices 0 and 2. The two occurrences overlap.
'''

s = input().strip()
p = input().strip()

m = len(p)

lps = [0] * m
length = 0
i = 1

while i < m:
    if p[i] == p[length]:
        length += 1
        lps[i] = length
        i += 1
    elif length > 0:
        length = lps[length - 1]
    else:
        i += 1

result = []
i = 0
j = 0

while i < len(s):
    if s[i] == p[j]:
        i += 1
        j += 1

        if j == m:
            result.append(i - m)
            j = lps[j - 1]
    elif j > 0:
        j = lps[j - 1]
    else:
        i += 1

print(len(result))

if result:
    print(*result)
else:
    print(-1)