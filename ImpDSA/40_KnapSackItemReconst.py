'''
Problem 40 — 0/1 Knapsack with Item Reconstruction

Topic: Dynamic Programming

Problem Statement

You are given N items. Each item has a weight and a value. You have a bag with maximum capacity W.

Each item can either be selected once or not selected at all.

Maximize the total value without exceeding the bag capacity. If multiple selections produce the same maximum value, choose the selection with the smallest number of items. If there is still a tie, choose the lexicographically smallest list of selected one-based item indices.

Input Format

The first line contains N and W.

Each of the next N lines contains weight value.

Output Format

Print three lines:

Maximum total value.

Total weight of the selected items.

The selected item indices in increasing order.

If no item is selected, print an empty third line.

Constraints

1 ≤ N ≤ 1000

1 ≤ W ≤ 10^5

1 ≤ weight[i] ≤ W

1 ≤ value[i] ≤ 10^6

Sample Input

4 7
3 10
4 20
2 15
5 18

Sample Output

35
6
2 3

Sample Explanation

Selecting items 2 and 3 gives:

Weight = 4 + 2 = 6

Value = 20 + 15 = 35
'''

n, capacity = map(int, input().split())

items = []

for _ in range(n):
    weight, value = map(int, input().split())
    items.append((weight, value))

# dp_value[w] = maximum value for capacity w
# dp_count[w] = minimum number of items for that value
dp_value = [0] * (capacity + 1)
dp_count = [0] * (capacity + 1)

# Store the selected indices for each capacity.
# This keeps the implementation straightforward for the given constraints.
dp_items = [[] for _ in range(capacity + 1)]

for i in range(n):
    weight, value = items[i]
    index = i + 1

    for w in range(capacity, weight - 1, -1):
        new_value = dp_value[w - weight] + value
        new_count = dp_count[w - weight] + 1
        new_items = dp_items[w - weight] + [index]

        if new_value > dp_value[w]:
            dp_value[w] = new_value
            dp_count[w] = new_count
            dp_items[w] = new_items

        elif new_value == dp_value[w]:
            if new_count < dp_count[w]:
                dp_count[w] = new_count
                dp_items[w] = new_items
            elif new_count == dp_count[w] and new_items < dp_items[w]:
                dp_items[w] = new_items

selected = dp_items[capacity]

total_weight = 0

for index in selected:
    total_weight += items[index - 1][0]

print(dp_value[capacity])
print(total_weight)

if selected:
    print(*selected)
else:
    print()