# Time O(n)
# Space O(n)
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        currMax = 0
        total = 0
        for key, value in counts.items():
            if value > currMax:
                currMax = value
                total = value
            elif value == currMax:
                total += value
        
        return total