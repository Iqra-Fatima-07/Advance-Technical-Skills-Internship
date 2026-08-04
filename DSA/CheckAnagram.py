class Solution:
    def isAnagram(self, s1, s2):

        if len(s1) != len(s2):
            return False

        freq1 = {}
        freq2 = {}

        for char in s1:
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1

        for char in s2:
            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1

        return freq1 == freq2


# Input
s1 = "listen"
s2 = "silent"

# Call function
obj = Solution()
answer = obj.isAnagram(s1, s2)

# Output
if answer:
    print("Anagram")
else:
    print("Not Anagram")