# Time O(n)
# Space O(n)
class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1

        max_unique = -1
        for key, value in hash_map.items():
            if value == 1 and key > max_unique:
                max_unique = key
        
        return max_unique
