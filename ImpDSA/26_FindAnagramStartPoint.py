'''
Problem 26 — Find All Anagram Starting Positions

Topic: Strings / Sliding Window

Problem Statement

Given strings S and P, find every starting index in S where an anagram of P occurs as a contiguous substring.

Two strings are anagrams if they contain exactly the same characters with the same frequencies.

Return all valid starting positions in increasing order.

Input Format

First line: string S

Second line: string P

Both contain lowercase English letters.

Output Format

First print the number of occurrences.

On the next line, print their zero-based starting indices in increasing order.

If there are no occurrences, print 0 on the first line and -1 on the second line.

Constraints

1 ≤ |P| ≤ |S| ≤ 2 × 10^5

Sample Input

cbaebabacd
abc

Sample Output

2
0 6

Sample Explanation

Anagrams of abc occur at:

index 0: cba

index 6: bac

Therefore the answer contains indices 0 and 6.
'''

s = input().strip()
p = input().strip()

n = len(s)
m = len(p)

pattern = [0] * 26
window = [0] * 26

for ch in p:
    pattern[ord(ch) - ord('a')] += 1

for i in range(m):
    window[ord(s[i]) - ord('a')] += 1

result = []

if window == pattern:
    result.append(0)

for i in range(m, n):
    window[ord(s[i]) - ord('a')] += 1
    window[ord(s[i - m]) - ord('a')] -= 1

    if window == pattern:
        result.append(i - m + 1)

print(len(result))

if result:
    print(*result)
else:
    print(-1)