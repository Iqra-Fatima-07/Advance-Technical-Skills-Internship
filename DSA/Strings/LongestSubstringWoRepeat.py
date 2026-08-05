#15. Longest Substring Without Repeating Characters A network monitoring system records a stream of unique packet IDs. 
# Find the length of the longest sequence without repetition. 
# Input: abcabcbb Output: 3

class Solution:

    def lengthOfLongestSubstring(self, s):

        left = 0
        seen = set()
        maxLength = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])


            length = right - left + 1


            maxLength = max(maxLength, length)

        return maxLength


s = "abcabcbb"


obj = Solution()
answer = obj.lengthOfLongestSubstring(s)

print("Longest length:", answer)