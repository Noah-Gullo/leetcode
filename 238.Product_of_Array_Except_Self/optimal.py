# Credit to [NeetCode](https://www.youtube.com/watch?v=bNvIQI2wAjk)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            curr_product = 1
            for j in range(len(nums)):
                if j != i:
                    curr_product *= nums[j]
            res.append(curr_product)

        return res