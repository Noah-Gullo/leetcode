# Time O(n)
# Space O(n)
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        counts = {}
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
    
        return counts.get(letter, 0) * 100 // len(s)