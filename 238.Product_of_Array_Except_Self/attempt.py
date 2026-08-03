# Time O(n^2)
# Explanation: Two nested for loops which loop over nums
# Space O(1)
# Explanation: No additional data structures beyond nums and res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            curr_product = 1
            for j in range(len(nums)): 
                if i != j:
                    curr_product *= nums[j]
            
            res.append(curr_product)

                    
        return res