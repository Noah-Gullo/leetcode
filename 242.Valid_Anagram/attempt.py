class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash_map = {}
        t_hash_map = {}

        for i in range(len(s)):
            if s[i] in s_hash_map:
                s_hash_map[s[i]] += 1
            else:
                s_hash_map[s[i]] = 1

        for i in range(len(t)):
            if t[i] in t_hash_map:
                t_hash_map[t[i]] += 1
            else:
                t_hash_map[t[i]] = 1
        
        for key, value in s_hash_map.items():
            if key not in t_hash_map:
                return False
            elif t_hash_map[key] != value:
                return False
        
        return True