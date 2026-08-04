class Solution:
    def MissingNumber(self,arr):
        n=5
        sum = 0
        NormalSum = n*(n+1)//2
        for i in range(len((arr))):
            sum = sum + arr[i]
        MissingNum = NormalSum - sum
        return MissingNum
arr = [1, 2, 3, 5]

# Call function
obj = Solution()
answer = obj.MissingNumber(arr)

# Output
print(answer)