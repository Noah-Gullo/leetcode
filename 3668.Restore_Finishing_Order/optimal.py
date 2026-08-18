class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        mylist = []
        for num in order:
            if num in friends:
                mylist.append(num)
        return mylist