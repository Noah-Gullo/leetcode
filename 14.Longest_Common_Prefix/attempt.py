class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        while prefix:
            found = True
            for i in range(len(strs)):
                if not strs[i].startswith(prefix):
                    prefix = prefix[:-1]
                    found = False
                    break
            if found:
                return prefix
        
        return ""
            