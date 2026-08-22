# Time O(n)
# Space O(1)
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        hash_table = {}
        copy = n
        score = 0
        while copy > 0:
            digit = copy % 10
            if digit in hash_table:
                hash_table[digit] += 1
            else:
                hash_table[digit] = 1
            copy //= 10
        
        for num in hash_table:
            score += num * hash_table[num]
        return score
