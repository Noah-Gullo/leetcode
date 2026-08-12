class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        start = 0 
        right = len(s) - 1
        end = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                start = left + 1
                end = right - 1

            left += 1
            right -= 1
        return s[start:end + 1]