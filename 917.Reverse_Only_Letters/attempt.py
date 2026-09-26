# Time O(n)
# Space O(n)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        res = list(s)
        while left < right:
            while left < right and s[left].isalpha() != True:
                left += 1
            
            while left < right and s[right].isalpha() != True:
                right -= 1
            
            if left >= right:
                break

            res[left], res[right] = res[right], res[left]

            left += 1
            right -= 1
        
        return "".join(res)