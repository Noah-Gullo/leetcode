class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        found = set()
        for i in range(len(nums)):
            if nums[i] in found:
                res.append(nums[i])
                if len(res) == 2:
                    break
            else:
                found.add(nums[i])

        return res
            