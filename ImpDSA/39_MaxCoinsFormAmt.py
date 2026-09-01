'''
Problem 39 — Minimum Coins to Form an Amount

Topic: Dynamic Programming

Problem Statement

You are given a collection of coin denominations and a target amount. You may use each coin denomination any number of times.

Find the minimum number of coins required to form exactly the target amount. If it is impossible, print -1.

Input Format

The first line contains N and T.

The second line contains N positive coin denominations.

Output Format

Print the minimum number of coins required, or -1 if the target cannot be formed.

Constraints

1 ≤ N ≤ 100

1 ≤ coin[i] ≤ 10^4

0 ≤ T ≤ 10^5

Sample Input

3 11
1 2 5

Sample Output

3

Sample Explanation

The amount 11 can be formed using:

5 + 5 + 1

Therefore, three coins are required.
'''

n, target = map(int, input().split())
coins = list(map(int, input().split()))

dp = [target + 1] * (target + 1)
dp[0] = 0

for amount in range(1, target + 1):
    for coin in coins:
        if coin <= amount:
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

if dp[target] == target + 1:
    print(-1)
else:
    print(dp[target])