class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
       
        sorted_chars = sorted(counts, key=counts.get, reverse=True)
        chars = []
        for char in sorted_chars:
            for _ in range(counts[char]):
                chars.append(char)
        
        return "".join(chars)