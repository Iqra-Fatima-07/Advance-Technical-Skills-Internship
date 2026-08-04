#9. Rotate Array by K Positions A circular conveyor belt contains N items. After every cycle, 
# the belt rotates K positions to the right. 
# Input: 5 
# 1 2 3 4 5 
# 2 
# Output:4 5 1 2 3

class Solution:
    def reverse(self,arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    def rotate_array(self, arr,k):

        n = len(arr)
        self.reverse(arr,n-k,n-1)
        self.reverse(arr,0,n-k-1)
        self.reverse(arr,0,n-1)

        return arr


n = 5
arr = [1, 2, 3, 4, 5]
k = 2

obj = Solution()
answer = obj.rotate_array(arr,k)

print(answer)