# Time O(N)
# Explanation: Loops thorugh every char
# Space O(1)
# Explanation: Allocates score
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)):
            if i != len(s) - 1:
                score += abs(ord(s[i + 1]) - ord(s[i]))
        
        return score