# Time O(n)
# Space O(1)
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        parity = nums1[0] % 2
        for i in range(len(nums1)):
            if nums1[0] % 2 != parity:
                return False
        return True