'''
Problem 47 — Group Anagrams

Topic: Strings, Hashing

Problem Statement

Given N strings, group together all strings that are anagrams of each other.

Two strings are anagrams if they contain the same characters with the same frequencies.

The order of groups does not matter.

Input Format

First line contains integer N.

Next N lines contain one string each.

Output Format

Print each group of anagrams on a separate line.

Constraints

1 ≤ N ≤ 10^4
1 ≤ |S| ≤ 100

Strings contain lowercase English letters.

Sample Input

6
eat
tea
tan
ate
nat
bat

Sample Output

eat tea ate
tan nat
bat

Sample Explanation

eat, tea, and ate contain the same characters. Similarly, tan and nat are anagrams.
'''

n = int(input())

groups = {}

for _ in range(n):
    word = input().strip()
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

for group in groups.values():
    print(*group)