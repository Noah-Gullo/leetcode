# Time O(n)
# Space O(n)
class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_dic = {}
        result = 0
        
        for a in arr:
            if a not in arr_dic:
                arr_dic[a] = 1
            else:
                arr_dic[a] += 1
        
        for num in arr:
            if num+1 in arr_dic:
                result += 1
        
        return result