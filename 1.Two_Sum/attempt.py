# Time O(n^2)
# Explanation: This solution loops through every number and for every following number checks if they sum to the target
# Space O(1)
# Explanation: Only curr, i, and j are allocated. No other data structures are used because I iterate through nums.
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