'''
Problem 41 — Rotate Array by K Positions

Topic: Arrays, Reversal Technique

Problem Statement

Given an array of N integers and an integer K, rotate the array to the right by K positions.

A rotation moves the last element to the first position while shifting all other elements one position to the right.

If K is greater than N, reduce it appropriately.

Input Format

First line contains integer N.

Second line contains N space-separated integers.

Third line contains integer K.

Output Format

Print the array after rotating it right by K positions.

Constraints

1 ≤ N ≤ 10^5
0 ≤ K ≤ 10^9
-10^6 ≤ arr[i] ≤ 10^6

Sample Input

7
1 2 3 4 5 6 7
3

Sample Output

5 6 7 1 2 3 4

Sample Explanation

Rotating the array right by 3 positions moves 5, 6, 7 to the beginning.
'''

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

k %= n

arr.reverse()
arr[:k] = reversed(arr[:k])
arr[k:] = reversed(arr[k:])

print(*arr)