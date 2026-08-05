#12. First Non-Repeating Character A communication system receives a message stream. 
# Find the first character that appears only once. 
# Input: swiss Output: w

class Solution:
    def FirstNonRepeatingChar(self, s):
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for char in s:
            if freq[char] == 1:
                return char

        return None

obj = Solution()
answer = obj.FirstNonRepeatingChar("swiss")

print(answer)