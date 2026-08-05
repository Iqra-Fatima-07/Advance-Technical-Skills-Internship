class Solution:
    def secondLargest(self, arr):
        
        largest = arr[0]
        second = arr[1]

        if second > largest:
            largest, second = second, largest

        for i in range(2, len(arr)):

            if arr[i] > largest:
                second = largest
                largest = arr[i]

            elif arr[i] > second and arr[i] != largest:
                second = arr[i]

        return second