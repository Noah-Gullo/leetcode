# Time O(n)
# Space O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAverage = 0
        currSum = 0
        left = 0
        right = k
        for i in range(k):
            maxAverage += nums[i]
            currSum += nums[i]
        maxAverage /= k

        while right < len(nums):
            currSum -= nums[left]
            currSum += nums[right]
            if currSum / k > maxAverage:
                maxAverage = currSum / k
            
            left += 1
            right += 1
        
        return maxAverage