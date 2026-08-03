class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        r=[]
        for i in range(0,len(nums)):
            s=s+nums[i]
            r.append(s)
        return r