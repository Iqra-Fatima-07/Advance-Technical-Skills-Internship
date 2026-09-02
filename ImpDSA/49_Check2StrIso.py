'''
Problem 49 — Check if Two Strings Are Isomorphic

Topic: Strings, Hashing

Problem Statement

Two strings are called isomorphic if characters in the first string can be consistently mapped to characters in the second string.

A character must always map to the same character, and two different characters cannot map to the same character.

Determine whether the two strings are isomorphic.

Input Format

First line contains string S.

Second line contains string T.

Output Format

Print YES if the strings are isomorphic; otherwise print NO.

Constraints

1 ≤ |S|, |T| ≤ 10^5

|S| = |T|

Sample Input

egg
add

Sample Output

YES

Sample Explanation

e → a and g → d. The mapping remains consistent throughout the strings.
'''

s = input().strip()
t = input().strip()

mapping = {}
mapped_to = {}

isomorphic = True

for a, b in zip(s, t):
    if a in mapping and mapping[a] != b:
        isomorphic = False
        break

    if b in mapped_to and mapped_to[b] != a:
        isomorphic = False
        break

    mapping[a] = b
    mapped_to[b] = a

if isomorphic:
    print("YES")
else:
    print("NO")