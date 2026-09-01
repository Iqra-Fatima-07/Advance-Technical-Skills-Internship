'''
Problem 21 — Trapping Rain Water

Topic: Two Pointers / Arrays

Problem Statement

Given an array where each element represents the height of a vertical bar of width 1, determine how much rainwater can be trapped between the bars after rainfall.

Water can be trapped only when there are taller bars on both sides of a position. Calculate the total volume of trapped water across the entire elevation map.

Input Format

The first line contains N.

The second line contains N non-negative integers representing bar heights.

Output Format

Print the total amount of trapped water.

Constraints

1 ≤ N ≤ 2 × 10^5
0 ≤ height[i] ≤ 10^9

Sample Input

12
0 1 0 2 1 0 1 3 2 1 2 1

Sample Output

6

Sample Explanation

Water is trapped between the taller bars. Adding the trapped water at all positions gives a total of 6 units.
'''

n = int(input())
height = list(map(int, input().split()))

left = 0
right = n - 1

left_max = 0
right_max = 0
water = 0

while left <= right:
    if height[left] <= height[right]:
        if height[left] >= left_max:
            left_max = height[left]
        else:
            water += left_max - height[left]
        left += 1
    else:
        if height[right] >= right_max:
            right_max = height[right]
        else:
            water += right_max - height[right]
        right -= 1

print(water)