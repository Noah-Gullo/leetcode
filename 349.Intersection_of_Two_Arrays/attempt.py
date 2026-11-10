# Time O(n)
# Space O(n)
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        res = set()
        for i in range(len(nums2)):
            if nums2[i] in set1:
                res.add(nums2[i])
        
        return list(res)

        