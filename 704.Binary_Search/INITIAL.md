Initial thoughts:
Get the middle element. mid = (left + right) // 2.  If nums[mid] < target then set left = mid + 1, if nums[mid] > target set right = mid - 1. If num[mid] == target return mid. 