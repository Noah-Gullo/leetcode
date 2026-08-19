class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            left = i
            right = i
            curr_len = 0
            while left > 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
                curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
        
        return max_len
