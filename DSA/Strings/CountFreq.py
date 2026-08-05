class Solution:
    def characterFrequency(self, s, ch):
        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        return freq[ch]


# Input
s = "TCSNQT"
ch = "T"

# Call function
obj = Solution()
answer = obj.characterFrequency(s, ch)

# Output
print("Frequency:", answer)