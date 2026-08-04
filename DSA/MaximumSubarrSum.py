#11. Maximum Subarray Sum A stock analyst records daily profit and loss values. 
#Find the maximum profit that can be obtained from a continuous sequence of days. 
#Input: 8-2 -3 4 -1 -2 1 5 -3 Output: 7
class Solution:
    def maxSubArraySum(self, arr):
        current_sum = 0
        Max_sum = 0

        for num in arr:
            current_sum += num
            if current_sum < 0:
                current_sum = 0
            elif current_sum > Max_sum:
                Max_sum = current_sum

        return Max_sum

obj = Solution()
answer = obj.maxSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4])

print(answer)