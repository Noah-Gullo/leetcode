# Time O(n) - Algorithm iterates through entire heights
# Space O(1) - only storing left, right, maxArea, and currArea
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            currArea = (right - left)*(min(height[left], height[right]))
            if currArea > maxArea:
                maxArea = currArea
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea