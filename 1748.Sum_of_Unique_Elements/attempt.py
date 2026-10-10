# Time O(n)
# Space O(n)
class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1

        res = 0
        for key, value in counts.items():
            if value == 1:
                res += key
        
        return res
