class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        index_map = {}
        
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in index_map:
                index_map[sorted_nums[i]] = i

        result = []

        for num in nums:
            result.append(index_map[num])

        return result