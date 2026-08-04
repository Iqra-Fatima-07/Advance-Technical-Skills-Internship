#13. Largest and Smallest Element An examination system stores marks of students. 
# Find the highest and lowest marks obtained. 
# Input: 5 45 90 67 23 88 Output: Largest = 90 Smallest = 23

class Solution:
    def largest_and_smallest(self, arr):
        largest = arr[0]
        smallest = arr[0]

        for num in arr:
            if num > largest:
                largest = num
            elif num < smallest:
                smallest = num

        return largest, smallest

obj = Solution()
answer = obj.largest_and_smallest([45, 90, 67, 23, 88])

print(answer)