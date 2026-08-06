# Time O(n)
# Explanation: Technically O(n/2) but O(n)
# Space O(n)
# Explanation: str(x) creates a new string of len(x) or len(n) 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        left = 0
        right = len(strx) - 1
        while left < right:
            if strx[left] != strx[right]:
                return False
            left += 1
            right -= 1 

        return True