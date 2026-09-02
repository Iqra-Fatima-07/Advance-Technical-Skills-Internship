'''
Problem 43 — Find the Missing Ranges

Topic: Arrays, Sorting

Problem Statement

You are given a sorted array of distinct integers and two integers lower and upper.

Find all ranges of numbers that are missing between lower and upper, inclusive.

Represent a single missing number as x and multiple consecutive missing numbers as x->y.

Input Format

First line contains integer N.

Second line contains N sorted integers.

Third line contains lower and upper.

Output Format

Print all missing ranges separated by spaces.

Constraints

0 ≤ N ≤ 10^5
0 ≤ lower ≤ upper ≤ 10^9

Sample Input

4
2 5 8 10
1 10

Sample Output

1 3->4 6->7 9

Sample Explanation

Between 1 and 10, the missing values are:

1

3,4

6,7

9
'''

n = int(input())

if n > 0:
    arr = list(map(int, input().split()))
else:
    arr = []

lower, upper = map(int, input().split())

result = []
prev = lower - 1

for num in arr + [upper + 1]:
    if num > prev + 1:
        start = prev + 1
        end = num - 1

        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))

    prev = num

print(*result)