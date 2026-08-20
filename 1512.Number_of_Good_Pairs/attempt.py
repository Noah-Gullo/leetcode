class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        hash_table = {}

        for num in nums:
            if num in hash_table:
                count += hash_table[num]
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        return count