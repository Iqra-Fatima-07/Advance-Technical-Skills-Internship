'''
Problem 24 — Permutation in a String

Topic: Sliding Window / Frequency Counting

Problem Statement

Given two lowercase English strings S and P, determine whether S contains a contiguous substring that is a permutation of P.

A substring is a permutation of P if it has exactly the same characters with exactly the same frequencies, although the order may differ.

Input Format

The first line contains string S.

The second line contains string P.

Output Format

Print YES if such a substring exists; otherwise print NO.

Constraints

1 ≤ |P| ≤ |S| ≤ 2 × 10^5

Both strings contain lowercase English letters.

Sample Input

eidbaooo
ab

Sample Output

YES

Sample Explanation

The substring ba is a permutation of ab, so the answer is YES.
'''

s = input().strip()
p = input().strip()

if len(p) > len(s):
    print("NO")
else:
    required = [0] * 26
    window = [0] * 26

    for ch in p:
        required[ord(ch) - ord('a')] += 1

    for i in range(len(p)):
        window[ord(s[i]) - ord('a')] += 1

    if window == required:
        print("YES")
    else:
        found = False

        for i in range(len(p), len(s)):
            window[ord(s[i]) - ord('a')] += 1
            window[ord(s[i - len(p)]) - ord('a')] -= 1

            if window == required:
                found = True
                break

        if found:
            print("YES")
        else:
            print("NO")