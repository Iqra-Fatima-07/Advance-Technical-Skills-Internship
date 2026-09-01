'''
9. Missing and Repeating Number

An array should contain every integer from 1 through N exactly once. One value appears twice and another value is missing. Find both.

INPUT FORMAT

Line 1: N
Line 2: N integers from 1 to N

SAMPLE INPUT

5
1 2 2 5 4

OUTPUT FORMAT

Print the repeated value followed by the missing value.

SAMPLE OUTPUT

2 3

EXPLANATION

2 is repeated and 3 is missing.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
'''

n = int(input())
arr = list(map(int, input().split()))

frequency = [0] * (n + 1)

for num in arr:
    frequency[num] += 1

repeating = -1
missing = -1

for i in range(1, n + 1):
    if frequency[i] == 2:
        repeating = i
    elif frequency[i] == 0:
        missing = i

print(repeating, missing)