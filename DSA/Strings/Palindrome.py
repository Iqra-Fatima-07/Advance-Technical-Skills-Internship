class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

# Input
s = "MADAM"

# Create object
obj = Solution()

# Call function
result = obj.isPalindrome(s)

# Output
if result:
    print("Palindrome")
else:
    print("Not Palindrome")