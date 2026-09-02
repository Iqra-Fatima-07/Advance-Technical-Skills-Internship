'''
Problem 42 — Sort Array by Frequency

Topic: Hashing, Sorting

Problem Statement

Given an array of integers, sort its elements according to their frequency.

Elements with higher frequency should appear first. If two elements have the same frequency, the smaller element should appear first.

Input Format

First line contains integer N.

Second line contains N space-separated integers.

Output Format

Print the frequency-sorted array.

Constraints

1 ≤ N ≤ 10^5
-10^5 ≤ arr[i] ≤ 10^5

Sample Input

8
4 5 6 5 4 4 6 5

Sample Output

4 4 4 5 5 5 6 6

Sample Explanation

4 and 5 both occur 3 times, so 4 comes before 5. 6 occurs twice and therefore comes after them.
'''

n = int(input())
arr = list(map(int, input().split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

arr.sort(key=lambda x: (-freq[x], x))

print(*arr)