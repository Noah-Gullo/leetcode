class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        hash_table = {}
        min_num = 100000
        max_num = -100000
        res = []
        for i in range(len(nums)):
            curr = nums[i]
            hash_table[curr] = i
            if curr < min_num:
                min_num = curr
            
            if curr > max_num:
                max_num = curr
        
        for i in range(min_num, max_num):
            if i not in hash_table:
                res.append(i)
        
        return res