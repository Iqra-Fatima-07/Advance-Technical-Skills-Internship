'''
8. Majority Element II

Given an integer array, find every value occurring strictly more than floor(N/3) times. At most two values can satisfy this condition.

INPUT FORMAT

Line 1: N
Line 2: N integers

SAMPLE INPUT

8
3 2 3 2 2 1 2 3

OUTPUT FORMAT

Print qualifying values in increasing order. Print -1 if none qualifies.

SAMPLE OUTPUT

2 3

EXPLANATION

2 occurs 4 times and 3 occurs 3 times; both > floor(8/3) = 2.

CONSTRAINTS

1 ≤ N ≤ 2 × 10^5
'''

n = int(input())
arr = list(map(int, input().split()))

candidate1 = None
candidate2 = None
count1 = 0
count2 = 0

for num in arr:
    if num == candidate1:
        count1 += 1
    elif num == candidate2:
        count2 += 1
    elif count1 == 0:
        candidate1 = num
        count1 = 1
    elif count2 == 0:
        candidate2 = num
        count2 = 1
    else:
        count1 -= 1
        count2 -= 1

count1 = 0
count2 = 0

for num in arr:
    if num == candidate1:
        count1 += 1
    elif num == candidate2:
        count2 += 1

result = []

if count1 > n // 3:
    result.append(candidate1)

if candidate2 != candidate1 and count2 > n // 3:
    result.append(candidate2)

result.sort()

if result:
    print(*result)
else:
    print(-1)