#14. Count Vowels and Consonants A language analyzer needs to count vowels and consonants present in a word. 
# Input:education Output: Vowels = 5 Consonants = 4

class Solution:
    def countVowelsConsonants(self, word):
        vowels = "aeiouAEIOU"
        vowel_count = 0
        consonant_count = 0
        for char in word:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        return vowel_count, consonant_count

obj = Solution()
word = "education"
vowel_count, consonant_count = obj.countVowelsConsonants(word)

print(f"Vowels = {vowel_count}, Consonants = {consonant_count}")