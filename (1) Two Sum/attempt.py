class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # Current number
            curr = nums[i];
            # Check if the current number a number after it equals 'target'. If it does return their indices.
            for j in range(i + 1, len(nums)):
                if curr + nums[j] == target:
                    return [i, j]
        
        return [];