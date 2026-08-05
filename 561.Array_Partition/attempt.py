class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum