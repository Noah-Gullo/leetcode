# Credit to [NeetCode](https://www.youtube.com/watch?v=Wwml2yq-qH4)
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        x = 0
        for n in nums:
            x = x ^ n
        
        for i in range(len(nums) - )2
            x = x ^ i

        diff_bit = x & -x
        xor1, xo2 = 0, 0
        for n in nums:
            if n & diff_bit:
                xor1 ^= n
            else:
                xor2 ^= n
        
        for n in nums:
            if i & diff_bit:
                xor1 ^= i
            else:
                xor2 ^= i

        return [xor1, xor2]

        