class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        res = [-1] * n
        
        if k == 0:
            return nums
        
        window = 2 * k + 1
        if window > n:
            return res
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for center in range(k, n - k):
            total = prefix[center + k + 1] - prefix[center - k]
            res[center] = total // window
        
        return res