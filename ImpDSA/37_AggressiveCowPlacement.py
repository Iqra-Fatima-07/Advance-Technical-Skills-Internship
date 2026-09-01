'''
Problem 37 — Aggressive Cow Placement

Topic: Binary Search on Answer / Greedy

Problem Statement

There are N stalls located at different positions along a straight line. You must place C cows into distinct stalls.

The goal is to maximize the minimum distance between any two cows.

Determine the largest possible value of this minimum distance.

Input Format

The first line contains N and C.

The second line contains N distinct stall positions.

Output Format

Print the maximum possible minimum distance.

Constraints

2 ≤ C ≤ N ≤ 2 × 10^5

0 ≤ position[i] ≤ 10^9

Sample Input

5 3
1 2 4 8 9

Sample Output

3

Sample Explanation

Cows can be placed at positions 1, 4, and 8.

The minimum distance is 3, and no arrangement can produce a larger minimum distance.
'''

n, cows = map(int, input().split())
positions = list(map(int, input().split()))

positions.sort()

def can_place(distance):
    count = 1
    last_position = positions[0]

    for position in positions[1:]:
        if position - last_position >= distance:
            count += 1
            last_position = position

            if count >= cows:
                return True

    return False

left = 0
right = positions[-1] - positions[0]

while left <= right:
    mid = (left + right) // 2

    if can_place(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)