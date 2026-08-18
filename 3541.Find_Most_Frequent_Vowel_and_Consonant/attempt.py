class Solution:
    def maxFreqSum(self, s: str) -> int:
        hash_table = {}
        for i in range(len(s)):
            if s[i].isalpha():
                if s[i] in hash_table:
                    hash_table[s[i]] += 1
                else:
                    hash_table[s[i]] = 1

        vowels = "aeiou"

        
        vowels = "aeiou"

        max_vowel = 0
        max_consonant = 0

        for char, freq in hash_table.items():
            if char in vowels:
                max_vowel = max(max_vowel, freq)
            else:
                max_consonant = max(max_consonant, freq)

        return max_vowel + max_consonant