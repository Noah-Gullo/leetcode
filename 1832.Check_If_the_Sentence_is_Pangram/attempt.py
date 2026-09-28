# Time O(n)
# Space O(n)
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hash_table = {}

        for i in range(len(sentence)):
            if sentence[i] in hash_table:
                hash_table[sentence[i]] += 1
            else:
                hash_table[sentence[i]] = 1
        
        return len(hash_table) == 26