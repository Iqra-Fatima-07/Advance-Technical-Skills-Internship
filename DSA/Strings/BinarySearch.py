#Binary Search
arr = [1,2,3,4,5,6,7,8,9,10]
target = 5
left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(f"Element found at index {mid}")
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Element not found")