'''
Problem 48 — String Compression

Topic: Strings, Two Pointers

Problem Statement

Compress a string by replacing consecutive repeated characters with the character followed by its frequency.

A character that occurs only once should still be followed by 1.

Input Format

A single line containing string S.

Output Format

Print the compressed string.

Constraints

1 ≤ |S| ≤ 10^5

The string contains lowercase English letters.

Sample Input

aaabbccccd

Sample Output

a3b2c4d1

Sample Explanation

a occurs consecutively 3 times → a3

b occurs 2 times → b2

c occurs 4 times → c4

d occurs once → d1
'''

s = input().strip()

result = []
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result.append(s[i - 1] + str(count))
        count = 1

result.append(s[-1] + str(count))

print(''.join(result))