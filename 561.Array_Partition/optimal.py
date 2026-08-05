# Credit [Arsalan Ahmed](https://www.youtube.com/watch?v=R7NepYjuloc)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        temp = 0
        for i in range(0, len(nums), 2):
            temp += nums[i]
        return temp