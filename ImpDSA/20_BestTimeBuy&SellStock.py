'''
20. Best Time to Buy and Sell Stock

Given the price of a stock for each day, choose exactly one day to buy and a later day to sell. Maximize the profit from this single transaction. If no profitable transaction is possible, return 0.

INPUT FORMAT

Line 1: N
Line 2: N daily prices

SAMPLE INPUT

6
7 1 5 3 6 4

OUTPUT FORMAT

Print the maximum possible profit.

SAMPLE OUTPUT

5

EXPLANATION

Buy at 1 and sell at 6 (profit = 5).

CONSTRAINTS

2 ≤ N ≤ 2 × 10^5
0 ≤ price[i] ≤ 10^9
'''

n = int(input())
prices = list(map(int, input().split()))

min_price = prices[0]
max_profit = 0

for price in prices[1:]:
    profit = price - min_price
    max_profit = max(max_profit, profit)

    min_price = min(min_price, price)

print(max_profit)