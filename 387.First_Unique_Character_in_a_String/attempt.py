# Time O(n)
# Space O()
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
        
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        
        return -1