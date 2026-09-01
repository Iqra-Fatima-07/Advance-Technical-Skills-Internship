'''
19. Insert Interval

You are given sorted, non-overlapping intervals and one new interval. Insert the new interval while preserving the sorted and non-overlapping properties. Merge every interval that overlaps the new interval.

INPUT FORMAT

Line 1: N
Next N lines: existing intervals
Final line: new_start new_end

SAMPLE INPUT

3
1 2
5 7
9 12
6 10

OUTPUT FORMAT

Print the resulting intervals, one per line.

SAMPLE OUTPUT

1 2
5 12

EXPLANATION

[6,10] overlaps [5,7] and [9,12], merging into [5,12].

CONSTRAINTS

0 ≤ N ≤ 2 × 10^5
'''

n = int(input())

intervals = []

for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

new_start, new_end = map(int, input().split())

result = []
i = 0

while i < n and intervals[i][1] < new_start:
    result.append(intervals[i])
    i += 1

while i < n and intervals[i][0] <= new_end:
    new_start = min(new_start, intervals[i][0])
    new_end = max(new_end, intervals[i][1])
    i += 1

result.append([new_start, new_end])

while i < n:
    result.append(intervals[i])
    i += 1

for start, end in result:
    print(start, end)