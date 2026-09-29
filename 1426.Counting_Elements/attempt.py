# Time O(n)
# Space O(n)
class Solution:
    def countElements(self, arr: list[int]) -> int:
        count = 0
        hash_set = set()
        for i in range(len(arr)):
            hash_set.add(arr[i])
        
        for i in range(len(arr)):
            if arr[i] + 1 in hash_set:
                count += 1
        
        return count