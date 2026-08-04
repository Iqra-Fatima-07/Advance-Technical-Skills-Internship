# find the second largest number in an array
arr = [1,2,3,4,5,6,8,7]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr[-2])

# OR

arr = [1,2,3,4,5,6,8,7]
arr.sort()
print(arr[-2])

#OR

arr = [1,2,3,4,5,6,8,7]
largest = second_largest = -1
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)