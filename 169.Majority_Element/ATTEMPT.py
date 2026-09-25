# Time O(n)
# Space O(n)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1
        
        for key, value in hash_table.items():
            if value > len(nums) / 2:
                return key