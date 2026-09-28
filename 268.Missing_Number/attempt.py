# Time O(n)
# Space O(n)
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        hash_set = set()
        for i in range(len(nums)):
            hash_set.add(nums[i])

        for i in range(0, len(nums) + 1):
            if i not in hash_set:
                return i
            