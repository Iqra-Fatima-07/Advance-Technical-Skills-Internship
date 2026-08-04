#10. Longest Word in a Sentence A text editor wants to highlight the longest word in a sentence for readability analysis.
#  Input: TCS coding practice is important Output: important

#python code
# s = "TCS coding practice is important"
# words = s.split()
# longest_word = max(words, key=len)
# print(longest_word)

#or

class Solution:
    def longestWord(self, sentence):
        
        words = sentence.split()
        longest = ""
        for word in words:
            if len(word) > len(longest):
                longest = word
        return longest

obj = Solution()
longest_word = obj.longestWord("TCS coding practice is important")
print(longest_word)