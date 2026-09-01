'''
18. Merge Overlapping Intervals

Given N closed intervals [start,end], merge every pair of intervals that overlap. The resulting intervals must be nonoverlapping and sorted by starting value.

INPUT FORMAT

Line 1: N
Next N lines: start end

SAMPLE INPUT

4
1 3
2 6
8 10
9 12

OUTPUT FORMAT

Print the merged intervals, one per line.

SAMPLE OUTPUT

1 6
8 12

EXPLANATION

[1,3] and [2,6] merge into [1,6]; [8,10] and [9,12] merge into [8,12].

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
start ≤ end
'''

n = int(input())

intervals = []

for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

intervals.sort()

merged = []

for start, end in intervals:
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

for start, end in merged:
    print(start, end)