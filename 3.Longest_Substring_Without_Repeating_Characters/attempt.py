class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       count, max_count = 0, 0
       start = 0
       last_seen = {}

       for i, c in enumerate(s):
        count = i - start + 1
        if c in last_seen and last_seen[c] >= start:
            start = last_seen[c] + 1
            count = i - start + 1
        
        if count > max_count:
            max_count = count
        
        last_seen[c] = i
        
       return max_count