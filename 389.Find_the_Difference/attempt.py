# Time O(n)
# Space O(1)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_map = {}
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1
        
        for i in range(len(t)):
            if t[i] in hash_map:
                hash_map[t[i]] -= 1
                if hash_map[t[i]] == 0:
                    del hash_map[t[i]]
            else:
                return t[i]
        
        return list(hash_map)[0]