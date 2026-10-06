class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, ones = 0, 0
        res = 0
        diff_index = {}

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                ones += 1

            diff = ones - zero

            if diff not in diff_index:
                diff_index[diff] = i

            if ones == zero:
                res = ones + zero
            else:
                res = max(res, i - diff_index[diff])

        return res