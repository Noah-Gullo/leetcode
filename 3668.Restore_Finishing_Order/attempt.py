class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = []
        hash_set = set()
        for i in range(len(friends)):
            hash_set.add(friends[i])
        
        for i in range(len(order)):
            if order[i] in hash_set:
                res.append(order[i])
        return res